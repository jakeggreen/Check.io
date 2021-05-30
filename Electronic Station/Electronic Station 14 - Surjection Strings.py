"""Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? i wish I know this word before.

You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.

One character from one string can correspond only to one character from another string. Two or more characters of one string can correspond to one character of another string, but not vice versa.

"""

def map_string(string) -> list:
	structure = []
	mappings = {}

	i = 1
	for char in string:
		if m := mappings.get(char):
			structure.append(m)
		else:
			mappings[char] = i
			i += 1
	return structure

def isometric_strings(str1: str, str2: str) -> bool:
	if len(set(list(str1))) != len(set(list(str2))):
		return False
	elif map_string(str1.lower()) == map_string(str2.lower()):
		return True
	else:
		return False

if __name__ == '__main__':
	print("Example:")
	print(isometric_strings('add', 'egg'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert isometric_strings('add', 'egg') == True
	assert isometric_strings('foo', 'bar') == False
	assert isometric_strings('', '') == True
	assert isometric_strings('all', 'all') == True
	assert isometric_strings("hall","hoop") == False
	print("Coding complete? Click 'Check' to earn cool rewards!")