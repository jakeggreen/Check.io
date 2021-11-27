"""Every year, the number of your friends is increasing and monitoring information about their lives is becoming more difficult. Let's simplify and slightly automate this process. Indeed, the simplification of routine processes is one of the key programming tasks.

You have to create a class ‘Person’ and a few methods to work with its instances. See the class description below.

class Person (first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown')

It returns a new instance of the ‘Person’ class with the name and surname [ first_name , last_name ], date of birth - birth_date (in 'dd.mm.yyyy' format), current job - job , number of working years - working_years , average salary - salary (per month), current country and city - [ country , city ] and gender - gender . The gender parameter could be 'male' or 'female'. If this parameter is undefined, the default value is - 'unknown'."""



from datetime import datetime
import math
import re

class Person:
	def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
		self.first_name = first_name
		self.last_name = last_name
		self.birth_date = birth_date
		self.job = job
		self.working_years = working_years
		self.salary = salary
		self.country = country
		self.city = city
		self.gender = gender

	def name(self):
		return f'{self.first_name} {self.last_name}'

	def age(self):
		birth_date = datetime.strptime(self.birth_date, '%d.%m.%Y').date()
		current_date = datetime.strptime('01.01.2018', '%d.%m.%Y').date()
		return math.floor(((current_date - birth_date).days)/365)

	def work(self):
		if self.gender == 'male':
			return f'He is a {self.job}'
		elif self.gender == 'female':
			return f'She is a {self.job}'
		else:
			return f'Is a {self.job}'

	def money(self):
		total_salary = self.working_years * (self.salary * 12)
		total_salary = re.sub(r'\,', ' ', "{:,}".format(total_salary))
		return total_salary

	def home(self):
		return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
	p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
	p3 = Person('Kate', 'Hound', '05.02.2000', 'student', 0, 0, 'Australia', 'Sydney', 'female')
	assert p1.name() == "John Smith", "Name"
	assert p1.age() == 38, "Age"
	assert p2.work() == "Is a designer", "Job"
	assert p1.money() == "648 000", "Money"
	assert p2.home() == "Lives in Vienna, Austria", "Home"
	assert p3.age() == 17, "Age"
	print("Coding complete? Let's try tests!")
