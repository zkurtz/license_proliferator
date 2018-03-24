from itertools import islice
import os
import re
import pdb

def select_target_files(repo_path,
                        file_exclude_pattern = None,
                        dir_exclude_pattern = None,
                        exclude_hidden_directories = True):
    '''
    :param repo_path: (str) Where to start recursively looking for files to modify
    :param file_exclude_pattern: (str) Any filename that matches this regular expression will be
    excluded
    :param dir_exclude_pattern: (str) Any directory name that matches this regular expression will
    be excluded
    :param exclude_hidden_directories: (boolean)
    :return: list of strings representing full file paths
    '''
    full_paths = []

    for root, dirs, files in os.walk(repo_path):
        if exclude_hidden_directories:
            dirs[:] = [d for d in dirs if not d[0] == '.']
        if dir_exclude_pattern:
            dirs[:] = [d for d in dirs if not re.match(dir_exclude_pattern, d)]
        if file_exclude_pattern:
            files[:] = [f for f in files if not re.match(file_exclude_pattern, f)]
        full_paths += [os.path.join(root, f) for f in files]

    return full_paths

def format_license(string, style = '# '):
    ''' Add comment markers to a string according to the specified style '''
    N = string.count('\n')
    if style == '# ':
        return style + string.replace("\n", "\n" + style, N-1)
    raise Exception('new style definition needed for ' + style)

def starts_with(file, string):
    N = string.count('\n')
    assert N > 0
    with open(file) as f:
        head = list(islice(f, N))
    return head == string

def prepend(license_file, files, styles = None, extra_blank_lines = 0):
    '''
    Prepend the content of a license file at the beginning of all files in a list

    :param license_file: (str) full path to file containing license text
    :param files: (list of str) full paths to files to have the license text prepended
    :param styles: (dict) key-value pairs where the key is a file extension str and the
    value is a function that converts a string to a comment string. If not specified,
    defaults to a reasonable choice for some common file type and '# '-prefixing for all others
    '''
    # Load license text
    with open(license_file) as lf:
        license_str = lf.read()
    if not license_str[-1:] == '\n':
        license_str += '\n'
    # Format the license
    # TODO: move some/all of this formatting inside the file loop after making it depend on file type
    ready_license_str = format_license(license_str)
    for file in files:
        if starts_with(file, ready_license_str):
            continue
        with open(file) as f:
            try:
                file_str = f.read()
            except:
                raise Exception('failed to read file ' + file)
        with open(file, 'w') as f:
            f.write(ready_license_str
                    + ''.join(['\n']*extra_blank_lines)
                    + file_str)