"""For the Robots the decimal format is inconvenient. If they need to count to "1", their computer brains want to count it in the binary representation of that number. You can read more about binary here .

You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1) are in the number spelling. For example: 5 = 0b101 contains two unities, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of unities in the binary form as an integer.
"""

# def checkio(number: int) -> int:
#     binary_number = bin(number)
#     unities = [int(x) for x in str(binary_number[2:]) if int(x) > 0]
#     return len(unities)

def checkio(number: int) -> int:
	return bin(number).count('1')

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
	assert checkio(4) == 1
	assert checkio(15) == 4
	assert checkio(1) == 1
	assert checkio(1022) == 9
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
