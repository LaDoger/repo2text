"""
This script is named "repo2text.py" and is designed to convert an entire
repository into a single .txt file named "repo2text.txt". This could be useful
when you want to feed the entire repository to a Large language Model (LLM) 
and let it understand how the repository works.

The script recursively goes through every file in the repository. It treats 
text-based files and non-text files differently:

- For text-based files, such as .py, .md, .txt, etc., it writes the file path 
  and the file content to "repo2text.txt".
  
- For non-text files, such as image or binary files, it only writes the file path
  to "repo2text.txt". 

Usage: 

- Put this python script named "repo2text.py" into the root folder of a repo.
- Execute "repo2text.py".
- The script will create "repo2text.txt" in the same root folder.
"""

import os
from pathlib import Path
import pathspec

# List of text-based file extensions
text_extensions = [
    # Common text and config files
    '.txt', '.json', '.xml', '.csv', '.yml', '.yaml', 

    # Scripting languages
    '.py', '.sh', '.bash', '.bat', '.cmd', '.pl', '.pm', '.t', '.pod', '.rb', '.lua', '.r', 

    # Web-related
    '.js', '.html', '.css', '.scss', '.sass', '.php', '.inc',

    # C and C++
    '.c', '.cpp', '.h', '.hpp', 

    # Java
    '.java', '.class',

    # Go, Rust, Swift
    '.go', '.rs', '.swift', 

    # .NET
    '.cs',

    # Functional programming
    '.m', '.erl', '.beam', '.ex', '.exs',

    # Smart contracts
    '.sol', '.vy',

    # Documentation and diagramming
    '.md', '.mmd',

    # Configurations
    '.cfg', '.conf', '.ini', '.properties', '.toml', '.prefs'
]

# List of special files with specific names
special_files = ['rebar.config', 'Dockerfile', 'Makefile', 'CMakeLists.txt']

# Default list of patterns to ignore
default_ignore_patterns = [
    '*.log', '*.bak', '*.swp', 
    '.DS_Store', '.Trash-*', '*.pyc', 
    '__pycache__', '*.obj', '*.exe', 
    '*.dll', '*.so', '*.dylib', '*.hi', '*.chi', 
    '*.pbc', '*.par', '*.pyo', '*.pyd', '*.pdb', 
    '*.asm', '*.bin', '*.elf', '*.hex', '*.lst', 
    '*.lss', '*.d', '*.dep', 'node_modules', 
    'venv/', 'venv/*', 'repo2text.py', 'repo2text.txt'
]

# Load .gitignore file if exists, otherwise use the default ignore list
try:
    with open('.gitignore', 'r') as f:
        gitignore = f.read()
    ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, gitignore.splitlines())
    print(".gitignore loaded.")
except FileNotFoundError:
    ignore_spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, default_ignore_patterns)
    print(".gitignore not found, using default ignore list.")

def should_ignore(file_path):
    relative_path = os.path.relpath(file_path, start=os.path.dirname(os.path.abspath(__file__)))
    if relative_path.split(os.sep)[0] == '.git' or relative_path == os.path.basename(__file__) or relative_path == 'repo2text.txt':
        print(f"Ignoring {relative_path} because it's in .git directory or is the script itself or the output file.")
        return True
    if ignore_spec.match_file(relative_path):
        print(f"Ignoring {relative_path} because it matches the ignore list.")
        return True
    print(f"Processing {relative_path}.")
    return False

def write_content(file_path, out_file, is_text_file):
    out_file.write("---\n`" + str(file_path) + "`:\n")
    if is_text_file:
        out_file.write("````\n")
        try:
            with open(file_path, 'r') as f:
                out_file.write(f.read())
            out_file.write("````\n")
        except Exception as e:
            print(f"Could not read file {file_path}. Reason: {e}")
    else:
        out_file.write("---\n")

def process_directory(dir_path, out_file):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = Path(root) / Path(file)
            if should_ignore(file_path):
                continue
            is_text_file = file_path.suffix in text_extensions or file in special_files
            write_content(file_path, out_file, is_text_file)

def main():
    with open('repo2text.txt', 'w') as out_file:
        process_directory('.', out_file)

if __name__ == "__main__":
    main()