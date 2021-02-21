def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start_idx = 0
    end_idx = len(array) - 1

    while start_idx <= end_idx:
        middle_idx = (start_idx + end_idx) // 2
        if array[middle_idx] == target:
            return middle_idx

        elif array[middle_idx] < target:
            start_idx = middle_idx - 1
        else:
            end_idx = middle_idx + 1
    return -1


def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        middle_element = array[middle_index]
    else:
        return -1

    if middle_element == target:
        return middle_index
    elif middle_element < target:
        return binary_search_recursive(array, target, middle_index - 1, end_index)
    else:
        return binary_search_recursive(array, target, start_index, middle_index + 1)


def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index


def contains(target, source):
    index = recursive_binary_search(target, source)
    if index is None:
        return False
    else:
        return True


def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index

    value_index = recursive_binary_search(number, arr)
    if value_index is None:
        return [-1, -1]

    first_index = value_index
    last_index = value_index

    if first_index > 0:
        while arr[first_index - 1] == number:
            first_index -= 1

    if last_index < len(arr) - 1:
        while arr[last_index + 1] == number:
            last_index += 1

    return [first_index, last_index]


if __name__ == '__main__':
    def test_function(test_case):
        answer = binary_search(test_case[0], test_case[1])
        if answer == test_case[2]:
            print("Pass!")
        else:
            print("Fail!")


    def test_function_2(test_case):
        answer = binary_search_recursive(test_case[0], test_case[1], 0, len(test_case[0]) - 1)
        if answer == test_case[2]:
            print("Pass!")
        else:
            print("Fail!")

    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    index = 6
    test_case = [array, target, index]
    test_function(test_case)

    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4
    index = 4
    test_case = [array, target, index]
    test_function_2(test_case)

    multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
    index = recursive_binary_search(7, multiple)
    multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
    print(find_first(7, multiple))  # Should return 3
    print(find_first(9, multiple))  # Should return None

    letters = ['a', 'c', 'd', 'f', 'g']
    print(contains('a', letters))  ## True
    print(contains('b', letters))  ## False


    def test_function(test_case):
        input_list = test_case[0]
        number = test_case[1]
        solution = test_case[2]
        output = first_and_last_index(input_list, number)
        if output == solution:
            print("Pass")
        else:
            print("Fail")


    input_list = [1]
    number = 1
    solution = [0, 0]
    test_case_1 = [input_list, number, solution]
    test_function(test_case_1)

    input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
    number = 3
    solution = [3, 6]
    test_case_2 = [input_list, number, solution]
    test_function(test_case_2)

    input_list = [0, 1, 2, 3, 4, 5]
    number = 5
    solution = [5, 5]
    test_case_3 = [input_list, number, solution]
    test_function(test_case_3)

    input_list = [0, 1, 2, 3, 4, 5]
    number = 6
    solution = [-1, -1]
    test_case_4 = [input_list, number, solution]
    test_function(test_case_4)