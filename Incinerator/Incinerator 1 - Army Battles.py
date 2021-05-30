"""In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But let's move to something that feels a little more epic - the armies! In this mission your task is to add new classes and functions to the existing ones. The new class should be the Army and have the method add_units() - for adding the chosen amount of units to the army. The first unit added will be the first to go to fight, the second will be the second, ...
Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and the surviving warrior continues to fight with his current health. This continues until all the soldiers of one of the armies die. In this case, the fight() function should return True , if the first army won, or False , if the second one was stronger.
Note that army 1 have the advantage to start every fight!"""

class Warrior():
	def __init__(self):
		self.health = 50
		self.attack = 5
		self.is_alive = True

	def make_attack(self, attacker, defender):
		defender.health = defender.health - attacker.attack
		if defender.health <= 0:
			defender.is_alive = False
			return defender.is_alive
		return defender.health

	def turn(self, unit_1, unit_2):
		unit_1.make_attack(unit_1, unit_2)
		if unit_2.is_alive == True:
			unit_2.make_attack(unit_2, unit_1)
			if unit_1.is_alive == True:
				unit_1.turn(unit_1, unit_2)
			else:
				unit_1.is_alive = False
				return unit_1.is_alive
		else:
			return unit_2.is_alive

class Knight(Warrior):
	def __init__(self):
		super().__init__()
		self.attack = 7

class Army():

	def add_units(self, soldier_type, units):
		army_size = []
		return army_size.extend([[soldier_type] for i in range(units)])

class Battle():

	def fight(self, army_1, army_2):
		pass

def fight(unit_1, unit_2):

	return unit_2.is_alive if unit_1.turn(unit_1, unit_2) else unit_1.is_alive

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	
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

	#battle tests
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

	print(my_army)

	assert battle.fight(my_army, enemy_army) == True
	assert battle.fight(army_3, army_4) == False
	print("Coding complete? Let's try tests!")
