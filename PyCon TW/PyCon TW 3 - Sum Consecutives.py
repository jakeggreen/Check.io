"""You are given a list that contains solely integers (positive and negative). Your job is to sum only the numbers that are identical and consecutive."""


def sum_consecutives(a):

	i, j, x = 0, 0, 0

	while a[i + 1] == a[i] and i < (len(a) -1):
		x += a[i] + a[i + 1]
		i += 1
		if i + 1 == len(a):
			return x
		print(x, j, i)



if __name__ == '__main__':
	print("Example:")
	print(list(sum_consecutives([1, 1, 1, 1])))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert list(sum_consecutives([1, 1, 1, 1])) == [4]
	assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
	assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
	assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
	assert list(sum_consecutives([1])) == [1]
	assert list(sum_consecutives([])) == []
	print("Coding complete? Click 'Check' to earn cool rewards!")
