"""You are given a text, which contains different English letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency , then return the letter which comes first in the Latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string."""

import re

def checkio(text: str) -> str:
	letter_dict = {}
	clean_text = re.sub(r'[^A-Za-z]', '', text).lower()
	for x in clean_text:
		entry = len(re.findall(x, clean_text))
		letter_dict[x] = entry
	sorted_dict = sorted(letter_dict, key=(lambda x: (-letter_dict.get(x), x)))
	return sorted_dict[0]

if __name__ == '__main__':
	print("Example:")
	print(checkio("Hello World!"))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio("Hello World!") == "l", "Hello test"
	assert checkio("How do you do?") == "o", "O is most wanted"
	assert checkio("One") == "e", "All letter only once."
	assert checkio("Oops!") == "o", "Don't forget about lower case."
	assert checkio("AAaooo!!!!") == "a", "Only letters."
	assert checkio("abe") == "a", "The First."
	print("Start the long test")
	assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
	print("The local tests are done.")
