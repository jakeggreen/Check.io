"""Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.

Output: a boolean."""

def is_all_upper(text: str) -> bool:
	text1 = text.replace(' ' ,'')
	if text.upper() == text or not text1.isalpha():
		return True
	else:
		return False


if __name__ == '__main__':
	print("Example:")
	print(is_all_upper('all lower'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert is_all_upper('ALL UPPER') == True
	assert is_all_upper('all lower') == False
	assert is_all_upper('mixed UPPER and lower') == False
	assert is_all_upper('') == True
	assert is_all_upper('     ') == True
	assert is_all_upper('444') == True
	assert is_all_upper('55 55 5') == True
	print("Coding complete? Click 'Check' to earn cool rewards!")