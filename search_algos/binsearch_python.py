'''
Basic implementation of the binary search algorithm in python.

'''


def binary_search(arr, l, r, val):
    '''
    Args:
    arr: a sorted list of integers to search for the target value.
    l: the index of the leftmost element in the search range.
    r: the index of the rightmost element in the search range.
    val: the value to be searched for in the list.
    '''
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            r = mid - 1
        else:
            l = mid + 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 0, len(arr) - 1, 3))