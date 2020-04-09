#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    return linear_search_recursive(array, item)
    # return linear_search_iterative(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array)-1:
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index+1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if array[mid] == item:
            return mid
        elif array[mid] < item:
            left = mid + 1
        else:  # array[mid] > item
            right = mid - 1
    return None


def binary_search_recursive(array, item, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array)-1
    if left > right:
        return None
    mid = int(left + (right - left) / 2)
    if array[mid] == item:
        return mid
    elif array[mid] < item:
        return binary_search_recursive(array, item, mid+1, right)
    else:  # array[mid] > item
        return binary_search_recursive(array, item, left, mid-1)
