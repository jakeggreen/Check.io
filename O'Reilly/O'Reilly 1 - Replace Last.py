"""In a given list the last element should become the first one. An empty list or list with only one element should stay the same

example

Input: List.

Output: Iterable."""

def replace_last(line: list) -> list:
	return [line[i] for i in range(-1,len(line)-1)]

if __name__ == '__main__':
	print("Example:")
	print(replace_last([2, 3, 4, 1]))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
	assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
	assert replace_last([1]) == [1]
	assert replace_last([]) == []
	print("Coding complete? Click 'Check' to earn cool rewards!")
