import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    b_list = []
    dir_list = os.listdir(path)

    for direction in dir_list:
        full_direction = os.path.join(path, direction)
        if os.path.isfile(full_direction):
            if full_direction.endswith(suffix):
                b_list.append(full_direction)
        else:
            b_list = b_list + find_files(suffix, full_direction)
    return b_list


if __name__ == '__main__':
    print(find_files('.c', 'testdir'))
