"""
Script to convert an entire repository into a single .txt file named "repo2text.txt".
This could be useful when you want to feed the entire repository to a
Large Language Model (LLM) and let it understand how the repository works.

Usage: 

- Put this python script named "repo2text.py" into the root folder of a repo.
- Execute "repo2text.py".
- The script will create "repo2text.txt" in the same root folder.
"""

import argparse
import pathspec
from pathlib import Path
from functools import lru_cache


# File extension categories
COMMON_FILES = ['.txt', '.json', '.xml', '.csv', '.yml', '.yaml']
SCRIPTING_LANGUAGES = ['.py', '.sh', '.rb', '.lua', '.r']
WEB_RELATED = ['.js', '.html', '.css', '.php']
C_CPP = ['.c', '.cpp', '.h', '.hpp']
JAVA = ['.java', '.class']
OTHER_LANGUAGES = ['.go', '.rs', '.swift', '.cs']
FUNCTIONAL_PROGRAMMING = ['.m', '.erl', '.beam', '.ex', '.exs']
SMART_CONTRACTS = ['.sol', '.vy']
DOCUMENTATION = ['.md', '.mmd']
CONFIGURATIONS = ['.cfg', '.conf', '.ini', '.properties', '.toml']

# List of text-based file extensions
text_extensions = COMMON_FILES + SCRIPTING_LANGUAGES + WEB_RELATED + C_CPP + JAVA + OTHER_LANGUAGES + FUNCTIONAL_PROGRAMMING + SMART_CONTRACTS + DOCUMENTATION + CONFIGURATIONS

# List of special files with specific names
special_files = ['rebar.config']

# Default list of patterns to ignore
default_ignore_patterns = [
    '*.log', '*.bak', '*.swp', 
    '.DS_Store', '.Trash-*', '*.pyc', 
    '__pycache__', '*.obj', '*.exe', 
    '*.dll', '*.so', '*.dylib', '*.hi', '*.chi', 
    '*.pbc', '*.par', '*.pyo', '*.pyd', '*.pdb', 
    '*.asm', '*.bin', '*.elf', '*.hex', '*.lst', 
    '*.lss', '*.d', '*.dep', 'node_modules', 
    '*.beam', 'LICENSE.md', '_build',
    'venv/', 'venv/*', 'repo2text.py', 'repo2text.txt',
    '.env', '.dockerignore', '.gitignore', '.github/'
]

class Repo2Text:
    def __init__(self, root_path: Path, output_file: Path):
        self.root_path = root_path
        self.output_file = output_file

        # Load .gitignore file if exists, otherwise use the default ignore list
        gitignore_file = self.root_path / '.gitignore'
        if gitignore_file.exists():
            with gitignore_file.open('r') as f:
                gitignore = f.read()
            self.ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, gitignore.splitlines())
            print(".gitignore loaded.")
        else:
            self.ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, default_ignore_patterns)
            print(".gitignore not found, using default ignore list.")

    @lru_cache(maxsize=None)
    def should_ignore(self, file_path: Path) -> bool:
        relative_path = file_path.relative_to(self.root_path)
        if '.git' in relative_path.parts or '.github' in relative_path.parts or str(relative_path) in {'repo2text.py', 'repo2text.txt', '.env', '.dockerignore', '.gitignore', 'LICENSE.md'}:
            print(f"Ignoring {relative_path} because it's in .git or .github directory or is the script itself or the output file.")
            return True
        if self.ignore_spec.match_file(str(relative_path)):
            print(f"Ignoring {relative_path} because it matches the ignore list.")
            return True
        print(f"Processing {relative_path}.")
        return False

    def write_content(self, file_path: Path, out_file):
        is_text_file = file_path.suffix in text_extensions or file_path.name in special_files
        should_ignore_file = self.should_ignore(file_path)
        
        if not should_ignore_file:  # Add this condition
            out_file.write(f"\n---\n`{str(file_path)}`\n")
            
            if is_text_file:
                out_file.write("````\n")
                try:
                    out_file.write(file_path.read_text(errors='replace'))
                except Exception as e:
                    print(f"Could not read file {file_path}. Reason: {e}")
                out_file.write("````\n")
                out_file.write("---\n")
            else:
                out_file.write("---\n")

    def process_directory(self, dir_path: Path):
        with self.output_file.open('w') as out_file:
            for file_path in sorted(dir_path.rglob('*')):
                if file_path.is_file() and not self.should_ignore(file_path):
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