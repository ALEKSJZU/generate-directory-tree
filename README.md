# Directory Tree Generator

This script generates a text representation of a directory tree, allowing for easy visualization of the directory's structure. It supports customizable depth levels and the ability to ignore specific file extensions.

## Features

- Generate a directory tree as a text file.
- Customizable depth to control how deep the tree should go.
- Ability to ignore files with specified extensions.

## Prerequisites

Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/).

## Installation

Clone this repository to your local machine using:

```bash
git clone https://github.com/YOURUSERNAME/generate-directory-tree.git
cd generate-directory-tree
```
##Usage

##To generate a directory tree, run the script from the command line:

python directory_tree_generator.py <directory> --output <output_file> --depth <depth> --ignore <extensions>
<directory>: The path to the directory you want to generate the tree for.
--output <output_file>: (Optional) The path to the output file. Defaults to directory_tree.txt.
--depth <depth>: (Optional) The maximum depth of the tree. Leave blank for no limit.
--ignore <extensions>: (Optional) Space-separated list of file extensions to ignore. Include the dot (e.g., .jpg .png).

##Example:
python directory_tree_generator.py /path/to/directory --output tree.txt --depth 3 --ignore .jpg .png

##Contributing
Contributions are welcome! Please feel free to submit a pull request.
