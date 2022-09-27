"""This mission is the part of the set. Another one - Caesar cipher decriptor .

Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.) using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance. For example ("a b c", 3) == "d e f"

Input: A secret message as a string (lowercase letters only and white spaces)

Output: The same string, but encrypted
"""

from string import ascii_lowercase

alpha_dict = {b : a for a, b in enumerate(ascii_lowercase, start = 1)}

number_dict = {a : b for a, b in enumerate(ascii_lowercase, start = 1)}

def create_num_list(text):
	num_list = []
	for x in text:
		if x.isalpha():
			num_list.append(alpha_dict.get(x))
		else:
			num_list.append(x)
	return num_list

def to_encrypt(text, delta):
	final_text = []
	data = create_num_list(text)
	for number in data:
		if type(number) == int:
			if (number + delta) % 26 == 0:
				number = 26
			else:
				number = (number + delta) % 26
			final_text.append(number_dict.get(number))
		else:
			final_text.append(number)
	return ''.join(final_text)
    

if __name__ == '__main__':
	print("Example:")
	print(to_encrypt('abc', 10))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert to_encrypt("a b c", 3) == "d e f"
	assert to_encrypt("a b c", -3) == "x y z"
	assert to_encrypt("simple text", 16) == "iycfbu junj"
	assert to_encrypt("important text", 10) == "swzybdkxd dohd"
	assert to_encrypt("state secret", -13) == "fgngr frperg"
	print("Coding complete? Click 'Check' to earn cool rewards!")
