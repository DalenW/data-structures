# implement a linear search

def linear_search(array: [], target):
	for i in range(len(array)):
		if array[i] == target:
			return i
	return -1