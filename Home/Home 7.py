"""In a given string you should reverse every word, but the words should stay in their places.

Input: A string.

Output: A string."""

#method 1 - splitting the string, reversing the elements and re-joining

# def backward_string_by_word(text: str) -> str:
# 	if not len(text) == 0: #deals with empty strings
# 		text = text.split(' ') #split on spaces making sure they're included
# 		reverse = list()
# 		for word in text:
# 			reverse.append(word[::-1]) #use slice to reverse each word
# 		return ' '.join(reverse) #join words back together including spaces
# 	return text

#condensed version

def backward_string_by_word(text: str) -> str:
	if not len(text) == 0: #deals with empty strings
		text = text.split(' ') #split on spaces making sure they're included
		reverse = [word[::-1] for word in text] #use slice to reverse each word
		reverse.append("x")
		return ' '.join(reverse) #join words back together including spaces
	return text

if __name__ == '__main__':
	print("Example:")
	print(backward_string_by_word(''))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert backward_string_by_word('') == ''
	assert backward_string_by_word('world') == 'dlrow'
	assert backward_string_by_word('hello world') == 'olleh dlrow'
	assert backward_string_by_word('hello   world') == 'olleh   dlrow'
	assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
	print("Coding complete? Click 'Check' to earn cool rewards!")


range(0,5)