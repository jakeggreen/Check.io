"""In a given text you need to sum the numbers. Only separated numbers should be counted. If a number is part of a word it shouldn't be counted.

The text consists from numbers, spaces and english letters

Input: A string.

Output: An int."""

#method 1 checking each word for letters and removing if alpha.
# def sum_numbers(text: str) -> int:
#     text = text.split(' ')
#     for word in text:
#     	if word.isalpha():
#     		text.remove(word)
#     print(text)

#method 2 - using regular expressions check is word contains numbers and or alpha characters
# import re

# def sum_numbers(text: str) -> int:
# 	summation = list()
# 	for word in text.split():
# 		if not re.search(r'[^0-9\s]+',word):
# 			summation.append(int(word))
# 	return(sum(summation))

#method 3 - condensed version without reg ex

def sum_numbers(text: str) -> int:
	return sum(int(x) for x in text.split() if x.isdigit())

if __name__ == '__main__':
	print("Example:")
	print(sum_numbers('daa3 d 63'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert sum_numbers('hi') == 0
	assert sum_numbers('who is 1st here') == 0
	assert sum_numbers('my numbers is 2') == 2
	assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
	assert sum_numbers('5 plus 6 is') == 11
	assert sum_numbers('') == 0
	print("Coding complete? Click 'Check' to earn cool rewards!")