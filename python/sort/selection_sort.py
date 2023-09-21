# implements a selection sort

def selection_sort1(array: []):
    unsorted_array: [] = array
    sorted_array: [] = []
    
    while len(unsorted_array) > 0:
        # find the smallest element in the unsorted array and put it in the sorted array
        smallest = unsorted_array[0]
        smallest_index: int = 0
        for i in range(len(unsorted_array)):
            if unsorted_array[i] < smallest:
                smallest = unsorted_array[i]
                smallest_index = i
        sorted_array.append(smallest)
        unsorted_array.pop(smallest_index)
    return sorted_array


def selection_sort2(array: []):
    """
    Implements another version of the selection sort
    """
    for i in range(len(array)):
        min_index: int = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array


def selection_sort3(array: []):
    """
    Implements another version of the selection sort
    """
    for i in range(len(array)-1):
      
        # Find index of smallest remaining element
        index_smallest: int = i
        for j in range(i+1, len(array)):
            if array[j] < array[index_smallest]:
                index_smallest = j
      
        # Swap array[i] and array[index_smallest]
        temp = array[i]
        array[i] = array[index_smallest]
        array[index_smallest] = temp