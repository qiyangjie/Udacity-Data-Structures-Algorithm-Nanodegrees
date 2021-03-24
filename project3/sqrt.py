def sqrt_help(left, right, number):
    if number < 0:
        return -1

    mid = (left + right + 1) // 2
    if mid * mid > number:
        right = mid
        mid = sqrt_help(left, right, number)
    elif number >= (mid+1) * (mid+1):
        left = mid
        mid = sqrt_help(left, right, number)

    return mid


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    return sqrt_help(0, number, number)


if __name__ == '__main__':
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    # Corner case
    print("Pass" if (-1 == sqrt(-9)) else "Fail")
    print("Pass" if (999 == sqrt(998001)) else "Fail")


