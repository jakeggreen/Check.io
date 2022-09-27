"""You often work with the different geometrical figures and with their parameters - the perimeter, area, and volume. You are tired of doing it manually, so you’ve decided to automate this process, and therefore you need to write a particular program. In this program you should create the class Parameters which will choose one of the few figures (the circle, regular triangle, square, regular pentagon, regular hexagon, cube) using the choose_figure() method and will count the perimeter, area, and volume with the help of the following methods:

perimeter() - returns the perimeter of the figure;
area() - returns the area of the figure;
volume() - returns the volume of the figure.

Also you have to create a class for each figure and use the Strategy design pattern to solve this mission.
Every figure, except the cube, has the volume = 0.
If the result has no decimal places, i you should return it as int(), n other case - round it to the 2 decimal points."""

from abc import ABC, abstractmethod
import math

class ShapeStrategy(ABC):
	@abstractmethod
	def area(self):
		pass

	def perimeter(self):
		pass

	def volume(self):
		pass

class Parameters():
	def __init__(self, length: int):
		self.length = length
		self.shape_strategy = None
		self.number_of_sides = None
  
	def choose_figure(self, shape_strategy = None):
		if shape_strategy is not None:
			self.shape_strategy = shape_strategy
   
	def area(self):
		return round(self.shape_strategy.area(self.length), 2)

	def perimeter(self):
		return round(self.shape_strategy.perimeter(self.length), 2)

	def volume(self):
		return round(self.shape_strategy.volume(self.length), 2)

class Circle(ShapeStrategy):

	number_of_sides = 1

	def area(self, length):
		squared_length = (length * length)
		return math.pi * squared_length

	def perimeter(self, length):
		return 2 * math.pi * length

	def volume(self, length):
		return 0
 
class Triangle(ShapeStrategy):
    
	number_of_sides = 3
    
	def area(self, length):
		s = (length * self.number_of_sides)/2
		s2 = (s - length)
		s3 = s * (s2 * s2 * s2)
		return math.sqrt(s3)

	def perimeter(self, length):
		return length * self.number_of_sides

	def volume(self, length):
		return 0

class Square(ShapeStrategy):
	
	number_of_sides = 4
 
	def area(self, length):
		return length ** 2

	def perimeter(self, length):
		return length * self.number_of_sides

	def volume(self, length):
		return 0

class Pentagon(ShapeStrategy):
	
	number_of_sides = 5
 
	def area(self, length):
		return 0.25 * (math.sqrt((5 * ( 5 + (2 * math.sqrt(5)))))) * (length ** 2)

	def perimeter(self, length):
		return length * self.number_of_sides

	def volume(self, length):
		return 0

class Hexagon(ShapeStrategy):
	
	number_of_sides = 6
 
	def area(self, length):
		return ((3 * math.sqrt(3)) / 2) * (length ** 2)

	def perimeter(self, length):
		return length * self.number_of_sides

	def volume(self, length):
		return 0

class Cube(ShapeStrategy):
	
	number_of_sides = 12
 
	def area(self, length):
		return 6 * (length ** 2)

	def perimeter(self, length):
		return length * self.number_of_sides

	def volume(self, length):
		return length ** 3

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	figure = Parameters(10)
	
	figure.choose_figure(Circle())
	assert figure.area() == 314.16

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
 
	figure = Parameters(5)
	figure.choose_figure(Triangle())
	assert figure.area() == 10.83

	print("Coding complete? Let's try tests!")
