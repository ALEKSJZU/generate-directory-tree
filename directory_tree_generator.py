import os
import argparse
def generate_directory_tree(dir_path, file_handle, prefix='', max_depth=None, ignore_extensions=None):
    if max_depth is not None and max_depth < 1:
        return

    if ignore_extensions is None:
        ignore_extensions = []

    files = []
    directories = []
    
    # Separate the directory contents into files and directories
    for item in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, item)):
            # Check file extension against ignore list
            if not any(item.endswith(ext) for ext in ignore_extensions):
                files.append(item)
        else:
            directories.append(item)
    
    # Write the directories first
    for directory in directories:
        file_handle.write(f"{prefix}+ {directory}\n")
        new_prefix = prefix + "|  "
        if max_depth is None or max_depth > 1:
            next_max_depth = None if max_depth is None else max_depth - 1
            generate_directory_tree(os.path.join(dir_path, directory), file_handle, new_prefix, next_max_depth, ignore_extensions)
    
    # Write the files in the current directory
    for file in files:
        file_handle.write(f"{prefix}- {file}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directory tree")
    parser.add_argument('directory', type=str, help='Directory path to generate tree for')
    parser.add_argument('--output', type=str, default='directory_tree.txt', help='Output file path')
    parser.add_argument('--depth', type=int, default=None, help='Maximum depth of tree')
    parser.add_argument('--ignore', nargs='*', default=[], help='File extensions to ignore')
    
    args = parser.parse_args()

    with open(args.output, 'w') as file_handle:
        generate_directory_tree(args.directory, file_handle, max_depth=args.depth, ignore_extensions=args.ignore)


