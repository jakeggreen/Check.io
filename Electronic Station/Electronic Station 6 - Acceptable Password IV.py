"""In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
Input: A string.

Output: A bool."""

# Taken from mission Acceptable Password III

def is_acceptable_password(password: str) -> bool:
	return True if len(password) > 6 else False

if __name__ == '__main__':
	print("Example:")
	print(is_acceptable_password('short'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert is_acceptable_password('short') == False
	assert is_acceptable_password('muchlonger') == True
	assert is_acceptable_password('ashort') == False
	print("Coding complete? Click 'Check' to earn cool rewards!")

import re

def is_acceptable_password(password: str) -> bool:
	return True if len(password) > 6 and re.search(r'\d+', password) else False

if __name__ == '__main__':
	print("Example:")
	print(is_acceptable_password('short'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert is_acceptable_password('short') == False
	assert is_acceptable_password('muchlonger') == False
	assert is_acceptable_password('ashort') == False
	assert is_acceptable_password('muchlonger5') == True
	assert is_acceptable_password('sh5') == False
	print("Coding complete? Click 'Check' to earn cool rewards!")

def is_acceptable_password(password: str) -> bool:
	return True if len(password) > 6 and re.search(r'\d+', password) and re.search(r'\D', password) else False


if __name__ == '__main__':
	print("Example:")
	print(is_acceptable_password('short'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert is_acceptable_password('short') == False
	assert is_acceptable_password('muchlonger') == False
	assert is_acceptable_password('ashort') == False
	assert is_acceptable_password('muchlonger5') == True
	assert is_acceptable_password('sh5') == False
	assert is_acceptable_password('1234567') == False
	print("Coding complete? Click 'Check' to earn cool rewards!")

def is_acceptable_password(password: str) -> bool:
	return True if (len(password) > 6 and re.search(r'\d+', password) and re.search(r'\D', password)) or (len(password) > 9) else False

if __name__ == '__main__':
	print("Example:")
	print(is_acceptable_password('short'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert is_acceptable_password('short') == False
	assert is_acceptable_password('short54') == True
	assert is_acceptable_password('muchlonger') == True
	assert is_acceptable_password('ashort') == False
	assert is_acceptable_password('muchlonger5') == True
	assert is_acceptable_password('sh5') == False
	assert is_acceptable_password('1234567') == False
	assert is_acceptable_password('12345678910') == True
	print("Coding complete? Click 'Check' to earn cool rewards!")
