"""In mathematics, particularly in linear algebra, a skew-symmetric matrix (also known as an antisymmetric or antimetric) is a square matrix A which is transposed and negative. This means that it satisfies the equation A = −A T . If the entry in the i-th row and j-th column is a ij , i.e. A = (a ij ) then the symmetric condition becomes a ij = −a ji .

You should determine whether the specified square matrix is skew-symmetric or not."""

def check_other(m, size):
	for x in m:
		y_cord = m.index(x)
		for y in x:
			x_cord = x.index(y)
			inverse_y = y_cord - 1
			inverse_x = x_cord - 1
			print(f'({y_cord},{x_cord}), ({inverse_y},{inverse_x})')

def check_corners(m, size):
	t_left = m[0][0]
	t_right = m[0][-1]
	b_left = m[-1][0]
	b_right = m[-1][-1]
	return True if t_left == (b_right * -1) and t_right == (b_left * -1) else False

def check_centre(m, size):
	return True if m[size^2][size^2] == 0 else False

def checkio(matrix):
	m_size = len(matrix)
	# if len(matrix) % 2 != 0:
	# 	centre = check_centre(matrix, m_size)
	# else:
	# 	centre = True
	# if centre or check_corners(matrix, m_size) == False:
	# 	return False
	check_other(matrix, m_size)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	print("Example:")
	print(checkio([
		[0, 1, 2],
		[-1, 0, 1],
		[-2, -1, 0]]))

	assert checkio([
		[0, 1, 2],
		[-1, 0, 1],
		[-2, -1, 0]]) == True, "1st example"
	assert checkio([
		[0, 1, 2],
		[-1, 1, 1],
		[-2, -1, 0]]) == False, "2nd example"
	assert checkio([
		[0, 1, 2],
		[-1, 0, 1],
		[-3, -1, 0]]) == False, "3rd example"
	print("Coding complete? Click 'Check' to earn cool rewards!");
