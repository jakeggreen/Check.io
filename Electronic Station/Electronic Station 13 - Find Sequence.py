"""You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence
Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean."""

from typing import List

def rec(matrix, position, direction, i = 0):

	while i < 4:
		x = direction[0] + position[0]
		y = direction[1] + position[1]
		start_number = matrix[position[0]][position[1]]
		if x >= 0 and y >= 0 and x <= len(matrix)-1 and y <= len(matrix)-1:
			coord_to_check = (x, y)
			number_at_coord = matrix[x][y]
			print(start_number, position, direction, coord_to_check, number_at_coord, f'i = {i}')
			if start_number == number_at_coord:
				i += 1
				rec(matrix, coord_to_check, direction, i)
			else:
				return False
		else:
			return False
	else:
		return True

def checkio(matrix: List[List[int]]) -> bool:

	length = range(0,len(matrix))

	directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

	coords = [(x, y) for x in length for y in length]

	# directions = [(0,1), (1,0), (0,-1), (-1,0)]

	print(coords)

	for coord in coords:
		for direction in directions:
			if rec(matrix, coord, direction):
				return True
			else:
				pass
	else:
		return False

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
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
		[1, 2, 1, 1],
		[1, 1, 4, 1],
		[1, 3, 1, 6],
		[1, 7, 2, 5]
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
