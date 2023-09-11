def binary_search(ls, key):
    """Returns the position of key in the list if found, -1 otherwise.

    The List must be sorted.
    """
    left = 0
    right = len(ls) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1
