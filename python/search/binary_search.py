# implements a binary search algorith. Assumes that the array is already sorted.

def binary_search(array: [], target):
    mid = len(array) // 2
    if array[mid] == target:
        return mid
    
    if array[mid] > target:
        return binary_search(array[:mid], target)
    else:
        return binary_search(array[mid:], target)