"""You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence
Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean."""

from typing import List

def checkio(matrix: List[List[int]]) -> bool:
	for row in range(0,len(matrix)-1):
		for column in range(0,len(matrix[0])-1):
			print(row,column)

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio([
		[1, 2, 1, 1],
		[1, 1, 4, 1],
		[1, 3, 1, 6],
		[1, 7, 2, 5]
	]) == True
	assert checkio([
		[7, 1, 4, 1],
		[1, 2, 5, 2],
		[3, 4, 1, 3],
		[1, 1, 8, 1]
	]) == False
	assert checkio([
		[2, 1, 1, 6, 1],
		[1, 3, 2, 1, 1],
		[4, 1, 1, 3, 1],
		[5, 5, 5, 5, 5],
		[1, 1, 3, 1, 1]
	]) == True
	assert checkio([
		[7, 1, 1, 8, 1, 1],
		[1, 1, 7, 3, 1, 5],
		[2, 3, 1, 2, 5, 1],
		[1, 1, 1, 5, 1, 4],
		[4, 6, 5, 1, 3, 1],
		[1, 1, 9, 1, 2, 1]
	]) == True
	print('All Done! Time to check!')
