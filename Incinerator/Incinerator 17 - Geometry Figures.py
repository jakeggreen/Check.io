"""You often work with the different geometrical figures and with their parameters - the perimeter, area, and volume. You are tired of doing it manually, so you’ve decided to automate this process, and therefore you need to write a particular program. In this program you should create the class Parameters which will choose one of the few figures (the circle, regular triangle, square, regular pentagon, regular hexagon, cube) using the choose_figure() method and will count the perimeter, area, and volume with the help of the following methods:

perimeter() - returns the perimeter of the figure;
area() - returns the area of the figure;
volume() - returns the volume of the figure.

Also you have to create a class for each figure and use the Strategy design pattern to solve this mission.
Every figure, except the cube, has the volume = 0.
If the result has no decimal places, you should return it as int(), in other case - round it to the 2 decimal points."""


class Parameters():
	def __init__(self, length: int, func=None, number_of_sides=None):
		self.length = length
		self.number_of_sides = None

		if func is not None:
			self.__class__(func)

	def choose_figure(self, class_type):
		self.__class__(class_type)

	
	def area(self):
		return self.length * self.length

	def perimeter(self):
		print(self.length, self.number_of_sides)
		return self.length * self.number_of_sides

	def volume(self):
		if not isinstance(self, Cube):
			return 0
		return self.length ** self.length

class Circle(Parameters):
	def __init__(self):
		super(). __init__(self)
	
	number_of_sides = 1

class Triangle(Parameters):
	def __init__(self):
		super(). __init__(self)
	
	number_of_sides = 3

class Square(Parameters):
	def __init__(self):
		super(). __init__(self)
	
	number_of_sides = 4

class Pentagon(Parameters):
	def __init__(self):
		super(). __init__(self)
	
	number_of_sides = 5

class Hexagon(Parameters):
	def __init__(self):
		super(). __init__(self)
	
	number_of_sides = 6

class Cube(Parameters):
	def __init__(self):
		super(). __init__(self)
	
	number_of_sides = 12


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	figure = Parameters(10)
	
	# figure.choose_figure(Circle())
	# assert figure.area() == 314.16

	figure.choose_figure(Triangle())
	assert figure.perimeter() == 30

	figure.choose_figure(Square())
	assert figure.area() == 100

	figure.choose_figure(Pentagon())
	assert figure.perimeter() == 50

	figure.choose_figure(Hexagon())
	assert figure.perimeter() == 60

	figure.choose_figure(Cube())
	assert figure.volume() == 1000

	print("Coding complete? Let's try tests!")
