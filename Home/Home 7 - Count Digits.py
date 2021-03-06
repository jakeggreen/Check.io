"""You need to count the number of digits in a given string.

Input: A Str.

Output: An Int."""

#method 1 - using a substitution to remove all non-digits
import re

def count_digits(text: str) -> int:
	return len(re.sub(r'[\D\s]','',text))

#method 2 - using a findall to find all figits

# return len(re.findall(r'[0-9]', text))

if __name__ == '__main__':
	print("Example:")
	print(count_digits('who is 1st here'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert count_digits('hi') == 0
	assert count_digits('who is 1st here') == 1
	assert count_digits('my numbers is 2') == 1
	assert count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
	assert count_digits('5 plus 6 is') == 2
	assert count_digits('') == 0
	print("Coding complete? Click 'Check' to earn cool rewards!")