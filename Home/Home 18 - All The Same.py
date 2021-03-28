"""In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool."""

from typing import List, Any

# def all_the_same(elements: List[Any]) -> bool:
# 	count = 0 
# 	for x in elements:
# 		count = elements.count(x)
# 	return True if count == len(elements) else False

#method 2 - converting to set to remove duplicates and checking set length 

def all_the_same(elements: List[Any]) -> bool:
	if len(elements) <= 0:
		result = True
	else:
		result = len(set(elements)) == 1
	return result

if __name__ == '__main__':
	print("Example:")
	print(all_the_same([1, 1, 1]))
	
	# These "asserts" are used for self-checking and not for an auto-testing
	assert all_the_same([1, 1, 1]) == True
	assert all_the_same([1, 2, 1]) == False
	assert all_the_same(['a', 'a', 'a']) == True
	assert all_the_same([]) == True
	assert all_the_same([1]) == True
	print("Coding complete? Click 'Check' to earn cool rewards!")
