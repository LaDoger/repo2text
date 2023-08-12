"""
Script to convert an entire repo into a single "repo2text.txt" file.
This could be useful when you want to feed the entire repo to a
Large Language Model (LLM) and let it understand how the repo works.

Usage: 
- Put this python script named "repo2text.py" in the folder you want to convert.
- Execute "repo2text.py".
- The script will create "repo2text.txt" in the same folder.
"""

import argparse
import pathspec
from pathlib import Path


# File types we want to include in "repo2text.txt"
include_files = {
    '.txt', '.json', '.xml', '.csv', '.yml', '.yaml',  # Text/Data files
    '.py', '.sh', '.rb', '.lua', '.r',  # Scripts
    '.js', '.html', '.css', '.php',  # Web files
    '.c', '.cpp', '.h', '.hpp',  # C/C++
    '.java', '.class',  # Java
    '.go', '.rs', '.swift', '.cs',  # Other languages
    '.m', '.erl', '.hrl', '.ex', '.exs', '.elm',  # Functional
    '.sol', '.vy',  # Contracts
    '.md', '.mmd',  # Docs
    '.cfg', '.conf', '.ini', '.properties', '.toml', '.config'  # Configs
}


# File patterns we want to exclude from "repo2text.txt"
default_ignore_patterns = {
    '*.log', '*.bak', '*.swp', '*.tmp',  # Common temporary files
    '*.pyc', '__pycache__', 'venv/', 'venv_old/',  # Python specific files and directories
    'node_modules/',  # Node.js dependencies
    'build/', 'dist/', 'out/', 'target/',  # Build and distribution folders
    'vendor/',  # Dependencies in some languages
    'log/',  # Common directory for log files
    '*.o', '*.a', '*.bin', '*.exe', '*.dll', '*.so',  # Binary and object files
    'repo2text.py', 'repo2text.txt'  # This tool itself
}


class Repo2Text:
    def __init__(self, output_file: Path):
        # Use the directory of the current script as the root path
        self.root_path = Path(__file__).parent
        # Ensure the output file is in the same directory as the script
        self.output_file = self.root_path / output_file

        gitignore_file = self.root_path / '.gitignore'
        if gitignore_file.exists():
            with gitignore_file.open('r') as f:
                gitignore = f.read()
        else:
            gitignore = ""
        ignore_patterns = list(set(gitignore.splitlines()).union(set(default_ignore_patterns)))
        self.ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, ignore_patterns)
        self.ignored_dirs = set()
        self.file_count = 0

    def should_ignore(self, file_path: Path) -> bool:
        relative_path = file_path.relative_to(self.root_path)

        # Construct path from root to file, checking each directory
        current_path = self.root_path
        for part in relative_path.parts:
            current_path = current_path / part
            relative_dir = current_path.relative_to(self.root_path)
            
            # Check for hidden folders/files or those in default_ignore_patterns
            if any(p.startswith('.') for p in relative_dir.parts) or any(pattern.strip('/*') == str(relative_dir) for pattern in default_ignore_patterns):
                if str(relative_dir) not in self.ignored_dirs:
                    self.ignored_dirs.add(str(relative_dir))
                    print(f"*Ignoring {relative_dir}" + ("/" if current_path.is_dir() else ""))
                return True

            # Check for patterns in gitignore
            if self.ignore_spec.match_file(str(relative_dir) + ("/" if current_path.is_dir() else "")):
                if str(relative_dir) not in self.ignored_dirs:
                    self.ignored_dirs.add(str(relative_dir))
                    print(f"*Ignoring {relative_dir}" + ("/" if current_path.is_dir() else ""))
                return True
        return False
    
    def file_priority(self, file_path: Path) -> int:
        """Get the priority for the file. Lower values have higher priority."""
        name = file_path.name

        # Assign priorities
        if name == "README.md" and file_path.parent == self.root_path:  # Root directory README.md
            return 0
        elif name == "README.md":  # Other README.md files
            return 1
        elif file_path.parent == self.root_path:  # Other files in root directory
            return 2
        elif any(part.startswith('.') for part in file_path.parts):  # Hidden files/folders
            return 4
        else:
            return 3
    
    def sort_files(self, file_list: list) -> list:
        """Sort files based on defined priorities."""
        return sorted(file_list, key=lambda f: (self.file_priority(f), str(f).lower()))

    def write_content(self, file_path: Path, out_file):
        is_to_include = file_path.suffix in include_files

        # Use relative path to root of the repo for the separators
        relative_file_path = file_path.relative_to(self.root_path)

        if is_to_include:
            separator_start = f"\n\n-------- START OF `{relative_file_path}` --------\n\n````\n"
            separator_end = f"\n````\n-------- END OF `{relative_file_path}` --------\n\n"

            content = file_path.read_text(errors='replace')
            lines_added = len(content.splitlines())
            
            self.file_count += 1

            out_file.write(separator_start)
            out_file.write(content)
            out_file.write(separator_end)
            print(f"Including {file_path.relative_to(self.root_path)}")
            print(f"          ({lines_added} lines)")
        else:
            omitted_message = f"\n-------- CONTENT OF `{relative_file_path}` IS OMITTED --------\n"
            out_file.write(omitted_message)
            print(f"*Omitting {file_path.relative_to(self.root_path)}")

    def process_directory(self, dir_path: Path):
        with self.output_file.open('w') as out_file:
            all_files = list(dir_path.rglob('*'))
            sorted_files = self.sort_files(all_files)
            for file_path in sorted_files:
                if file_path.is_file():
                    should_ignore_file = self.should_ignore(file_path)
                    if not should_ignore_file:
                        self.write_content(file_path, out_file)
        self.print_recap()

    def print_recap(self):
        with self.output_file.open('r') as out_file:
            content = out_file.read()
            char_count = len(content)
            line_count = len(content.splitlines())
        print("\n===== RECAP: =====")
        print(f"Total files: {self.file_count}")
        print(f"Total chars: {char_count}")
        print(f"Total lines: {line_count}")


def main():
    parser = argparse.ArgumentParser(description='Convert a directory into a single .txt file.')
    parser.add_argument('--output', type=str, default='repo2text.txt', help='Name of the output file.')
    args = parser.parse_args()

    repo2text = Repo2Text(Path(args.output))
    repo2text.process_directory(repo2text.root_path)


if __name__ == "__main__":
    main()