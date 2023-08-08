"""
Script to convert an entire repo into a single .txt file named "repo2text.txt".
This could be useful when you want to feed the entire repo to a
Large Language Model (LLM) and let it understand how the repo works.

Usage: 

- Put this python script named "repo2text.py" into the root folder of a repo.
- Execute "repo2text.py".
- The script will create "repo2text.txt" in the same root folder.
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
    '.m', '.erl', '.ex', '.exs',  # Functional
    '.sol', '.vy',  # Contracts
    '.md', '.mmd',  # Docs
    '.cfg', '.conf', '.ini', '.properties', '.toml', '.config'  # Configs
}

# File patterns we want to exclude from "repo2text.txt"
default_ignore_patterns = {
    # Common temporary and backup files
    '*.log', '*.bak', '*.swp', '*.tmp',

    # Python specific files
    '*.pyc', '__pycache__', 'venv/', 'venv_old/',

    # Compiled binaries and related files
    '*.obj', '*.exe', '*.dll', '*.so', '*.dylib', 
    '*.hi', '*.chi', '*.pbc', '*.par', '*.pyo', 
    '*.pyd', '*.pdb', '*.asm', '*.bin', '*.elf', 
    '*.hex', '*.lst', '*.lss', '*.d', '*.dep',

    # Miscellaneous
    'node_modules', '*.beam', 'LICENSE', 'LICENSE.md', '_build',
    
    # This tool itself
    'repo2text.py', 'repo2text.txt'
}


def file_priority(file_path: Path) -> int:
    """Get the priority for the file. Lower values have higher priority."""
    name = file_path.name
    path_parts = file_path.parts

    # Assign priorities
    if name == "README.md":
        return 0
    elif file_path.parent == Path("."):  # Root directory
        return 1
    elif any(part.startswith('.') for part in path_parts):  # Hidden files/folders
        return 3
    else:
        return 2

def sort_files(file_list: list) -> list:
    """Sort files based on defined priorities."""
    return sorted(file_list, key=lambda f: (file_priority(f), str(f).lower()))


class Repo2Text:
    def __init__(self, root_path: Path, output_file: Path):
        self.root_path = root_path
        self.output_file = output_file

        gitignore_file = self.root_path / '.gitignore'
        if gitignore_file.exists():
            with gitignore_file.open('r') as f:
                gitignore = f.read()
        else:
            gitignore = ""
        ignore_patterns = list(set(gitignore.splitlines()).union(set(default_ignore_patterns)))
        self.ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, ignore_patterns)
        self.ignored_dirs = set()

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

        print(f"Including {relative_path}")
        return False

    def write_content(self, file_path: Path, out_file):
        is_text_file = file_path.suffix in include_files
        
        out_file.write(f"\n---\n`{str(file_path)}`\n")
            
        if is_text_file:
            out_file.write("````\n")
            try:
                out_file.write(file_path.read_text(errors='replace'))
            except Exception as e:
                print(f"Could not read file {file_path}. Reason: {e}")
            out_file.write("````\n")
        out_file.write("---\n")

    def process_directory(self, dir_path: Path):
        with self.output_file.open('w') as out_file:
            all_files = list(dir_path.rglob('*'))
            sorted_files = sort_files(all_files)
            for file_path in sorted_files:
                if file_path.is_file():
                    should_ignore_file = self.should_ignore(file_path)
                    if not should_ignore_file:
                        self.write_content(file_path, out_file)


def main():
    parser = argparse.ArgumentParser(description='Convert a repository into a single .txt file.')
    parser.add_argument('--path', type=str, default='.', help='Path to the root of the repository.')
    parser.add_argument('--output', type=str, default='repo2text.txt', help='Name of the output file.')
    args = parser.parse_args()

    repo2text = Repo2Text(Path(args.path), Path(args.output))
    repo2text.process_directory(repo2text.root_path)


if __name__ == "__main__":
    main()