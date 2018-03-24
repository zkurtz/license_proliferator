# License proliferator

Prepend every file in a repo with a block of license text while skipping over irrelevant files and directories.

WARNING: Use with caution. This tool involves modifying files in bulk and has not been substantially tested.

TODO: This code currently pre-pends inserted license text with
"# " code commenting syntax. Some generalization is obviously
needed to deal with various other commenting style

## Installation

Informally tested only with Python 3 and OSX High Sierra.

- Clone this repository
- `cd license_proliferator`
- `python setup.py install`

## Usage example

Step 1: Make a backup copy of the repo you're about to modify!

```python
import license_proliferator as lp

repo_path = '/Users/me/mycloud/repos/blp'
license_file = '/Users/me/mycloud/repos/blp/demo/pretend_license.txt'

file_list = lp.select_target_files(
    repo_path,
    dir_exclude_pattern = '(__pycache__|(.*)\.egg-info)',
    file_exclude_pattern = '(README(.*)|LICENSE.txt|pretend_license.txt)',
    exclude_hidden_directories = True
)
lp.prepend(license_file, file_list, extra_blank_lines = 1)

```

