def heapsort(array):
    heapify(array, len(array), 0)


def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """

    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        heapify(arr, n, largest_index)


def heapsort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


if __name__ == '__main__':
    arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
    solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
    solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [99]
    solution = [99]
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 1, 2, 5, 12, 21, 0]
    solution = [0, 0, 1, 2, 5, 12, 21]
    test_case = [arr, solution]
    test_function(test_case)



