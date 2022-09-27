"""Your task in this mission is to truncate a sentence to a length that does not exceed a given number of characters.

If the given sentence already is short enough, you don't have to do anything to it. But if it needs to be truncated, the omission must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.

The shortened sentence can contain complete words and spaces.
It must neither contain truncated words nor trailing spaces.
The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.

Input: Two arguments:

one-line sentence as a string,
max length of the truncated sentence as an int.
Output: The shortened sentence plus the ellipsis (if required) as a one-line string."""

from re import I


def cut_sentence(line: str, length: int) -> str:
	'''
	Cut a given sentence, so it becomes shorter than or equal to a given length.
	'''
	
	b = 1 
	a = line[length]

	while a.isalpha():
		a = line[length - b]
		b += 1
	print(line[:length - (b + 1)] + '...')
 
 
 
	# length = length - 1
	# if len(line) <= length:
	# 	return line

	# split_line = line.split()
	
	# i = 0
	# j = 0
	# for word in split_line:
	# 	if len(word) <= length:
	# 		i += 1
	# 		j += len(word)
	# 	if j >= length:
	# 		break
	# print(i, j)

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert cut_sentence("Hi my name is Alex", 4) == "Hi...", "First"
	assert cut_sentence("Hi my name is Alex", 8) == "Hi my...", "Second"
	assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex", "Third"
	assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex", "Fourth"
	print('Done! Do you like it? Go Check it!')
