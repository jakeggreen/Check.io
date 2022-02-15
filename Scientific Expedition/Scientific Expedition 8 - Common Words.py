"""Let's continue examining words. You are given two strings with words separated by commas. Try to find what is common between these strings. The words in the same string don't repeat.

Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings.

Output: The common words as a string."""

def checkio(line1: str, line2: str) -> str:
	common_words = list(set(line1.split(',')).intersection(set(line2.split(','))))
	return ','.join(sorted(list(common_words)))

if __name__ == '__main__':
	print("Example:")
	print(checkio('hello,world', 'hello,earth'))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert checkio('hello,world', 'hello,earth') == 'hello'
	assert checkio('one,two,three', 'four,five,six') == ''
	assert checkio('one,two,three', 'four,five,one,two,six,three') == 'one,three,two'
	print("Coding complete? Click 'Check' to earn cool rewards!")
