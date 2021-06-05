"""In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender. It should be the subclass of the Warrior class and have an additional defense parameter, which helps him to survive longer. When another unit hits the defender, he loses a certain amount of his health according to the next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.
The basic parameters of the Defender:
health = 60
attack = 3
defense = 2"""


class Warrior():

	attack = 5
	health = 50
	is_alive = True
	unit_type = 'Warrior'
	defence = 0

	def make_attack(self, defender):
		if (self.attack - defender.defence) < 0:
			attack = 0 
		else:
			attack = (self.attack - defender.defence)
		defender.health -= attack
		if defender.health <= 0:
			defender.is_alive = False

class Knight(Warrior):

	def __init__(self):
		super().__init__()

	attack = 7
	unit_type = 'Knight'

class Defender(Warrior):
	
	def __init__(self):
		super().__init__()

	health = 60
	attack = 3
	defence = 2
	unit_type = 'Defender'

class Rookie(Warrior):

	def __init__(self):
		super().__init__()

	health = 50
	attack = 1

class Army(list):

	def add_units(self, unit_type, no_of_units):
		for i in range(no_of_units): self.append(unit_type())
		return self

	def is_army_alive(self):
		return any([x.is_alive for x in self])

	def first_alive_unit(self):
		for unit in self:
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


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	
	#fight tests
	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()
	bob = Defender()
	mike = Knight()
	rog = Warrior()
	lancelot = Defender()

	assert fight(chuck, bruce) == True
	assert fight(dave, carl) == False
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False
	assert fight(bob, mike) == False
	assert fight(lancelot, rog) == True

	#battle tests
	my_army = Army()
	my_army.add_units(Defender, 1)
	
	enemy_army = Army()
	enemy_army.add_units(Warrior, 2)

	army_3 = Army()
	army_3.add_units(Warrior, 1)
	army_3.add_units(Defender, 1)

	army_4 = Army()
	army_4.add_units(Warrior, 2)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == False
	assert battle.fight(army_3, army_4) == True
	print("Coding complete? Let's try tests!")
