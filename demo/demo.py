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
