"""This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)"""

from typing import List, Tuple
Coords = List[Tuple[int, int]]

import math

# use the math library acos to find the arccos of each angle
def find_angles(a, b, c):
	first_angle = (b**2 + c**2 - a**2) / (2*b*c)
	second_angle = (a**2 + c**2 - b**2) / (2*a*c)
	third_angle = (a**2 + b**2 - c**2) / (2*a*b)
	angle_a = round(math.acos(first_angle),4)
	angle_b = round(math.acos(second_angle),4)
	angle_c = round(math.acos(third_angle),4)
	return [angle_a, angle_b, angle_c]

# find three lengths of sides of triangle, find the semi perimeter and then the area of triangle.

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
	#find length of sides between points, A-B, B-C, C-A for both triangles
	coord_list = (coords_1, coords_2)
	angles = []
	for coord in coord_list:
		a = math.sqrt(((coord[0][0] - coord[2][0]) ** 2) + ((coord[0][1] - coord[2][1]) ** 2))
		b = math.sqrt(((coord[0][0] - coord[1][0]) ** 2) + ((coord[0][1] - coord[1][1]) ** 2))
		c = math.sqrt(((coord[1][0] - coord[2][0]) ** 2) + ((coord[1][1] - coord[2][1]) ** 2))
		# print(f'Lengths: {a}, {b}, {c}')
		angles.append(find_angles(a, b, c))
		# print(angles)
	return True if set(angles[0]) == set(angles[1]) else False
	
if __name__ == '__main__':
	print("Example:")
	print(similar_triangles([[0, 2], [1, 4], [5, 2]], [[0, 1], [1, 3], [5, 1]]))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
	assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
	assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
	assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
	assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
	assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
	assert similar_triangles([[1, 3], [4, 2], [2, 1]], [[2, -2], [0, -3], [-1, -1]]) is True
	assert similar_triangles([[1, 2], [-3, 1], [-2, 5]], [[10, 10], [-10, 5], [5, -10]]) is True
	print("Coding complete? Click 'Check' to earn cool rewards!")
