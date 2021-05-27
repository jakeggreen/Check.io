"""You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence
Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean."""

from typing import List

# def rec(matrix, location, directions: list, i):

# 	while i < 3:
# 		for direction in directions:
# 			x = location[0] + direction[0]
# 			y = location[1] + direction[1]
# 			start_number = matrix[location[0]][location[1]]
# 			if not (x or y) < 0:
# 				coord_to_check = (x, y)
# 				number_at_coord = matrix[x][y]
# 				print(start_number, location, direction, coord_to_check, number_at_coord)
# 				if start_number == number_at_coord:
# 					i += 1
# 					rec(matrix, coord_to_check, direction, i)
# 				else:
# 					i = 0
# 					pass
# 			else:
# 				pass
# 	else:			
# 		print("True")
# 		return True

def checkio(matrix: List[List[int]]) -> bool:

	length = range(0,len(matrix))

	# directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

	coords = [(x, y) for x in length for y in length]

	directions = [(0,1), (1,0), (0,-1), (-1,0)]

	print(coords)

	i = 1
	while i < 4:
		for location in coords:
			for direction in directions:
				x = location[0] + (i * direction[0])
				y = location[1] + (i * direction[1])
				start_number = matrix[location[0]][location[1]]
				if not (x or y) < 0:
					coord_to_check = (x, y)
					number_at_coord = matrix[x][y]
					print(start_number, location, direction, coord_to_check, number_at_coord, f'i = {i}')
					if start_number == number_at_coord:
						i += 1
					else:
						i = 1
						pass
	else:
		return True

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
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
		[7, 1, 4, 1],
		[1, 2, 5, 2],
		[3, 4, 1, 3],
		[1, 1, 8, 1]
	]) == False

	assert checkio([
		[7, 1, 1, 8, 1, 1],
		[1, 1, 7, 3, 1, 5],
		[2, 3, 1, 2, 5, 1],
		[1, 1, 1, 5, 1, 4],
		[4, 6, 5, 1, 3, 1],
		[1, 1, 9, 1, 2, 1]
	]) == True
	print('All Done! Time to check!')
