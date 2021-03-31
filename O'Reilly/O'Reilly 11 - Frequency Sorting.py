"""Your mission is to sort the list by the frequency of numbers included in it. If a few numbers have an equal frequency - they should be sorted according to their natural order. For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]

Input: Chaotic list of numbers.

Output: The list of numbers in which they are sorted by their frequency."""

def frequency_sorting(numbers):
	sorted_numbers = sorted(numbers, reverse=True)
	final_sort = sorted(sorted_numbers, key= lambda x: (sorted_numbers.count(x), sorted_numbers.index(x)), reverse=True)
	return final_sort

if __name__ == '__main__':
	print("Example:")
	print(frequency_sorting([1, 2, 3, 4, 5]))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
	assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
	assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
	print("Coding complete? Click 'Check' to earn cool rewards!")
