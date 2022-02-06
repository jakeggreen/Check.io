"""While traveling, the spaceship endures quite a lot of stress. As a result, an important part of the maintenance is to check the outer hull. Stephan uses a digital durabilitimeter for this task. The device scans a portion of the spaceships hull and gives a durability map that is divided by small square fragments with measurements. Sometimes Stephan does not have much time and he can patch only couple points, so we need an algorithm to find the weak points.

The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell. To find the weakest point we should find the weakest row and column. The weakest point is placed in the intersection of these rows and columns. Row (column) durability is a sum of cell durability in that row (column). You should find coordinates of the weakest point (row and column). The first row (column) is 0th row (column). If a section has several equal weak points, then choose the closest point to the top edge and if there are multiple points closest to the top edge, then choose from those points the point that is closest to the left edge."""

def add_columns(matrix):
	return list(map(sum, zip(*matrix)))

def add_rows(matrix):
	row_totals_list = []
	for x in matrix:
		row_total = sum(x)
		row_totals_list.append(row_total)
	return row_totals_list

def weak_point(matrix):
	min_row = add_rows(matrix).index(min(add_rows(matrix)))
	min_col = add_columns(matrix).index(min(add_columns(matrix)))
	return (min_row, min_col)

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
	assert list(weak_point([[7, 2, 7, 2, 8],
							[2, 9, 4, 1, 7],
							[3, 8, 6, 2, 4],
							[2, 5, 2, 9, 1],
							[6, 6, 5, 4, 5]])) == [3, 3], "Example"
	assert list(weak_point([[7, 2, 4, 2, 8],
							[2, 8, 1, 1, 7],
							[3, 8, 6, 2, 4],
							[2, 5, 2, 9, 1],
							[6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
	assert list(weak_point([[1, 1, 1],
							[1, 1, 1],
							[1, 1, 1]])) == [0, 0], "Top left"
