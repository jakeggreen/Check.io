"""Nicola has solved this puzzle (and I am sure that you will do equally well). To be prepared for more such puzzles, Nicola wants to invent a method to search for words inside poetry. You can help him create a function to search for certain words.

You are given a rhyme (a multiline string), in which lines are separated by "newline". Casing does not matter for your search, but whitespaces should be removed before your search. You should find the word inside the rhyme in the horizontal (from left to right) or vertical (from up to down) lines. For this you need envision the rhyme as a matrix (2D array). Find the coordinates of the word in the cut rhyme (without whitespaces).

The result must be represented as a list -- [row_start,column_start,row_end,column_end], where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.
Counting of the rows and columns start from 1.

Input: Two arguments. A rhyme as a string and a word as a string (lowercase).

Output: The coordinates of the word."""

import re 

coords = [[0, 1], [1, 0]] #E, S

def search_coords(x, y, str_list, word, i, final_coords, start_length):
	for direction in coords:
		x_new = x + direction[0]
		y_new = y + direction[1]
		try:
			next_letter = str_list[y_new][x_new]
			print(f'Original Coords: {[x, y]}, direction: {direction}, New letter: {next_letter}, Looking for: {word[i + 1]}')
			if next_letter == word[i + 1]:
				start_length += 1
				if next_letter == word[-1] and start_length == len(word):
					print('HERE')
					if direction[0] == 0:
						final_coords.append([(y_new + 1) - (len(word) - 1), x_new + 1, y_new + 1, x_new + 1])
					if direction[1] == 0:
						final_coords.append([y_new + 1, (x_new + 1) - (len(word) - 1), y_new + 1, x_new + 1])
				i += 1
				search_coords(x_new, y_new, str_list, word, i, final_coords, start_length)
			else:
				pass
		except Exception:
			pass

def prepare_text(text: str):
	text = re.sub(r'[^\n\S\w]', '', text.lower())
	return text

def checkio(text, word):
	i = 0
	line = 0
	start_length = 1
	indexes = []
	final_coords = []
	text = prepare_text(text)
	text_list = text.split('\n')
	print(text)
	for string in text_list:
		index = [x.start() for x in re.finditer(word[i], string)] #list of 1st letters
		if len(index) == 0:
			pass
		elif len(index) > 1:
			for number in index:
				indexes.append([number, line])
		else:
			index = [str(i) for i in index]
			index = int(''.join(index))
			indexes.append([index, line])
		line += 1

	print(indexes)
	for index in indexes:
		x = index[0]
		y = index[1]
		search_coords(x, y, text_list, word, i, final_coords, start_length)

	return final_coords[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
	assert checkio("""DREAMINGofapplesonawall,
Anddreamingoften,dear,
Idreamedthat,ifIcountedall,
-Howmanywouldappear?""", "ten") == [2,14,2,16]
	assert checkio("""AndhastthouslaintheJabberwock?
Cometomyarms,mybeamishboy!
Ofrabjousday!Callooh!Callay!'
Hechortledinhisjoy.
'Twasbrillig,andtheslithytoves
Didgyreandgimbleinthewabe;
Allmimsyweretheborogoves,
Andthemomerathsoutgrabe.'""", "tomy") == [2,5,2,8]
	assert checkio("""Hiall!
Andallgoodbye!
Ofcoursegoodbye.
ornot""", "haoo") == [1,1,4,1]
print("Coding complete? Click 'Check' to earn cool rewards!")

