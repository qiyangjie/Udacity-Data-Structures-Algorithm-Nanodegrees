def ordered_array_search_recursive(input_list, number, begin_index, end_index):

    if input_list[begin_index] == number:
        return begin_index

    if end_index - begin_index <= 0:
        return -1

    current_index = (begin_index + end_index + 1) // 2
    mid = input_list[current_index]
    if mid == number:
        return current_index
    elif mid > number:
        return ordered_array_search_recursive(input_list, number, begin_index, current_index)
    else:
        return ordered_array_search_recursive(input_list, number, current_index, end_index)


# def rotated_array_search_recursive(input_list, number, begin_index, end_index):
#     current_index = (begin_index + end_index) // 2
#
#     begin = input_list[begin_index]
#     mid = input_list[current_index]
#     end = input_list[end_index]
#
#     if mid > begin and mid > end:
#         # left is sorted and right is unsorted
#         if number == mid:
#             return current_index
#         elif mid < number:
#             return rotated_array_search_recursive(input_list, number, current_index, end_index)
#         elif mid > number >= begin:
#             return ordered_array_search_recursive(input_list, number, begin_index, current_index)
#         elif mid > number and number < begin:
#             return rotated_array_search_recursive(input_list, number, current_index, end_index)
#     elif begin < mid < end:
#         # The list is sorted
#         if number == mid:
#             return current_index
#         elif mid < number:
#             return ordered_array_search_recursive(input_list, number, current_index, end_index)
#         elif mid > number:
#             return ordered_array_search_recursive(input_list, number, begin_index, current_index)
#     elif begin > mid:
#         # left is unsorted and right is sorted
#         if number == mid:
#             return current_index
#         elif mid < number:
#             if number < end:
#                 return ordered_array_search_recursive(input_list, number, current_index, end_index)
#             else:
#                 return rotated_array_search_recursive(input_list, number, begin_index, current_index)
#         elif mid > number:
#             return rotated_array_search_recursive(input_list, number, begin_index, current_index)
#     else:
#         return -1


def rotated_array_search_recursive(input_list, number, begin_index, end_index):
    current_index = (begin_index + end_index) // 2

    begin = input_list[begin_index]
    mid = input_list[current_index]
    end = input_list[end_index]

    if mid > begin and mid > end:
        # left is sorted and right is unsorted
        if number == mid:
            return current_index
        elif mid < number:
            return rotated_array_search_recursive(input_list, number, current_index, end_index)
        elif mid > number >= begin:
            return ordered_array_search_recursive(input_list, number, begin_index, current_index)
        elif mid > number and number < begin:
            return rotated_array_search_recursive(input_list, number, current_index, end_index)
    elif begin > mid:
        # left is unsorted and right is sorted
        if number == mid:
            return current_index
        elif mid < number:
            if number < end:
                return ordered_array_search_recursive(input_list, number, current_index, end_index)
            else:
                return rotated_array_search_recursive(input_list, number, begin_index, current_index)
        elif mid > number:
            return rotated_array_search_recursive(input_list, number, begin_index, current_index)
    else:
        return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       number:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_search_recursive(input_list, number, 0, len(input_list)-1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
