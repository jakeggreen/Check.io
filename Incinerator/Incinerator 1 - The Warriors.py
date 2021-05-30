"""I'm sure that many of you have some experience with computer games. But have you ever wanted to change the game so that the characters or a game world would be more consistent with your idea of the perfect game? Probably, yes.
In this mission (and in several subsequent ones, related to it) you’ll have a chance "to sit in the developer's chair" and create the logic of a simple game about battles.
Let's start with the simple task - one-on-one duel. You need to create the class Warrior , the instances of which will have 2 parameters - health (equal to 50 points) and attack (equal to 5 points), and 1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case). In addition you have to create the second unit type - Knight, which should be the subclass of the Warrior but have the increased attack - 7. Also you have to create a function fight() , which will initiate the duel between 2 warriors and define the strongest of them. The duel occurs according to the following principle:
Every turn, the first warrior will hit the second and this second will lose his health in the same value as the attack of the first warrior. After that, if he is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them. If the first warrior is still alive (and thus the other one is not anymore), the function should return True , False otherwise."""

class Warrior():
	def __init__(self):
		self.health = 50
		self.attack = 5
		self.is_alive = True


	def make_attack(self, attacker, defender):
		# print(f'Attacker hits defender for {attacker.attack}.')
		defender.health = defender.health - attacker.attack
		# print(f'Defender has {defender.health} health remaining')
		if defender.health <= 0:
			defender.is_alive = False
			return defender.is_alive
		return defender.health

	def turn(self, unit_1, unit_2):
		# print(f'unit 1 attacks unit 2')
		unit_1.make_attack(unit_1, unit_2)
		if unit_2.is_alive == True:
			# print(f'unit 2 attacks unit 1')
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

def fight(unit_1, unit_2):

	return unit_2.is_alive if unit_1.turn(unit_1, unit_2) else unit_1.is_alive


if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	chuck = Warrior()
	bruce = Warrior()
	carl = Knight()
	dave = Warrior()
	mark = Warrior()

	assert fight(dave, carl) == False
	assert fight(chuck, bruce) == True
	assert chuck.is_alive == True
	assert bruce.is_alive == False
	assert carl.is_alive == True
	assert dave.is_alive == False
	assert fight(carl, mark) == False
	assert carl.is_alive == False

	print("Coding complete? Let's try tests!")