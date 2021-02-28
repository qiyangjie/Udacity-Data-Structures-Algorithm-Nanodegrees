def find_median(Arr, start, size):
    myList = []
    for i in range(start, start + size):
        myList.append(Arr[i])

    myList.sort()

    return myList[size // 2]


def fastSelect(array, k):
    n = len(array)

    if 0 < k <= n:
        setOfMedians = []
        arr_less_P = []
        arr_equal_P = []
        arr_more_P = []
        i = 0

        while i < n // 5:
            median = find_median(array, 5 * i, 5)
            setOfMedians.append(median)
            i += 1

        if 5 * i < n:
            median = find_median(array, 5 * i, n % 5)
            setOfMedians.append(median)

        if len(setOfMedians) == 1:
            pivot = setOfMedians[0]
        elif len(setOfMedians) > 1:
            pivot = fastSelect(setOfMedians, len(setOfMedians) // 2)

        for element in array:
            if element < pivot:
                arr_less_P.append(element)
            elif element > pivot:
                arr_more_P.append(element)
            else:
                arr_equal_P.append(element)

        if k <= len(arr_less_P):
            return fastSelect(arr_less_P, k)
        elif k > (len(arr_less_P) + len(arr_equal_P)):
            return fastSelect(arr_more_P, (k - len(arr_less_P) - len(arr_equal_P)))
        else:
            return pivot


if __name__ == '__main__':
    Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
    k = 5
    print(fastSelect(Arr, k))  # Outputs 12

    Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
    k = 5
    print(fastSelect(Arr, k))  # Outputs 11

    Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
    k = 10
    print(fastSelect(Arr, k))  # Outputs 99
