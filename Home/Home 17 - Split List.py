"""You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.

Input: Array.

Output: Array or two arrays."""

# def split_list(items: list) -> list:
# 	array_1 = []
# 	array_2 = []
# 	if len(items) % 2 == 0:
# 		mid_point = int((len(items)/2))
# 		array_1 = items[0:mid_point]
# 		array_2 = items[mid_point:len(items)]
# 	else:
# 		mid_point = int((len(items)/2)+1)
# 		array_1 = items[0:mid_point]
# 		array_2 = items[mid_point:len(items)]
# 	return [array_1,array_2]


#method 2 - condensing above; not declaring the array, start or end of slice (default values)

def split_list(items: list) -> list:
	mid_point = int((len(items)+1) // 2)
	return [items[:mid_point],items[mid_point:]]


if __name__ == '__main__':
	print("Example:")
	print(split_list([1, 2, 3, 4, 5, 6]))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
	assert split_list([1, 2, 3]) == [[1, 2], [3]]
	assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
	assert split_list([1]) == [[1], []]
	assert split_list([]) == [[], []]
	print("Coding complete? Click 'Check' to earn cool rewards!")
