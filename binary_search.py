def upper_bound(array, val) -> int:
    """
    array: One dimensional iterable
    val: atomic numeric value (int, float, ...)

    Returns the first index greater than to the given value
    """
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2
        if array[mid] <= val:
            left = mid + 1
        else:
            right = mid

    return left


def lower_bound(array, val) -> int:
    """
    array: One dimensional iterable
    val: atomic numeric value (int, float, ...)

    Returns the first index greater than or equal to the given value
    """
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2
        if array[mid] >= val:
            right = mid
        else:
            left = mid + 1

    return left
