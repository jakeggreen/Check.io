"""In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But let's move to something that feels a little more epic - the armies! In this mission your task is to add new classes and functions to the existing ones. The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army. The first unit added will be the first to go to fight, the second will be the second, ...
Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the fight() function should return True , if the first army won, or False , if the second one was stronger.
Note that army 1 have the advantage to start every fight!"""

class Unit():

	#storing these as class attributes instead of instance attributes 
	#because default values available to all child classes

	health = 50
	is_alive = True

	def make_attack(self, defender):
		defender.health -= self.attack
		if defender.health <= 0:
			defender.is_alive = False

class Warrior(Unit):

	def __init__(self):
		super().__init__()

	attack = 5
	unit_type = 'Warrior'

class Knight(Unit):

	def __init__(self):
		super().__init__()

	attack = 7
	unit_type = 'Knight'
	
class Army():
	def __init__(self):
		self.army = []

	def __iter__(self):
		return iter(self.army)

	def add_units(self, unit_type, no_of_units):
		for i in range(no_of_units): self.army.append(unit_type())
		return self.army

	def is_army_alive(self):
		return any([x.is_alive for x in self.army])

	def first_alive_unit(self):
		for unit in self.army:
			if unit.is_alive == True:
				return unit
		return False

class Battle():

	#define a turn, find the first unit in active army where is_alive = true then have it fight with first unit in passive army where is_alive = true. If no is_alive = True return a winner.

	def fight(self, army_1, army_2):

		while army_1.is_army_alive() and army_2.is_army_alive():	
			attacker_unit = army_1.first_alive_unit()
			defender_unit = army_2.first_alive_unit()
			fight(attacker_unit, defender_unit)
		else:
			return army_1.is_army_alive()

def fight(unit_1, unit_2):

	turn = 1

	while unit_1.is_alive == True and unit_2.is_alive == True:
		if turn % 2 != 0:
			unit_1.make_attack(unit_2)
		else:
			unit_2.make_attack(unit_1)
		turn += 1
	else:
		return unit_1.is_alive

if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	
	#fight tests
	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()

	assert fight(chuck, bruce) == True
	assert fight(dave, carl) == False
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False

	# battle tests
	my_army = Army()
	my_army.add_units(Knight, 3)
	
	enemy_army = Army()
	enemy_army.add_units(Warrior, 3)

	army_3 = Army()
	army_3.add_units(Warrior, 20)
	army_3.add_units(Knight, 5)
	
	army_4 = Army()
	army_4.add_units(Warrior, 30)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == True
	assert battle.fight(army_3, army_4) == False
	print("Coding complete? Let's try tests!")
