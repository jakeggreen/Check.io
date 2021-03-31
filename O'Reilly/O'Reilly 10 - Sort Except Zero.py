"""Sort the numbers in an array. But the position of zeros should not be changed.

Input: A List.

Output: An Iterable (tuple, list, iterator ...)."""

#method 1 - using a bubble sort - this doesn't deal with the zeros.

from typing import Iterable

# def except_zero(items: list) -> Iterable:
# 	# we go through the list as many times as there are elements
# 	for i in range(len(items)):
# 		# we want the last pair of adjacent elements to be (n-2, n-1)
# 		for j in range(len(items) - 1):
# 			if items[j] > items[j+1]:
# 				# swap
# 				items[j], items[j+1] = items[j+1], items[j]
# 	return items

#method 2 - finding the index of the zeros, removing them, sorting the list then readding them

def except_zero(items: list) -> Iterable:
	#find indexes of zeros
	pos = []
	for i in range(len(items)):
		if items[i] == 0: 
			pos.append(i)
	number_of_zeros = len(pos)
	#sort the list and remove zeros
	items = sorted(items, reverse=False)
	items = items[number_of_zeros::]
	#add zeros back in at their indexes above
	for index in pos:
		items.insert(index,0)
	return(items)

if __name__ == '__main__':
	print("Example:")
	print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
	assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
	assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
	assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
	assert list(except_zero([0, 0])) == [0, 0]
	print("Coding complete? Click 'Check' to earn cool rewards!")
