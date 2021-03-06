"""The battle continues and each army is losing good warriors. Let's try to fix that and add a new unit type - the Healer.
Healer won't be fighting (his attack = 0, so he can't deal the damage). But his role is also very important - every time the allied soldier hits the enemy, the Healer will heal the allie, standing right in front of him by +2 health points with the heal() method. Note that the health after healing can't be greater than the maximum health of the unit. For example, if the Healer heals the Warrior with 49 health points, the Warrior will have 50 hp, because this is the maximum for him.
The basic parameters of the Healer:
health = 60
attack = 0"""

# Taken from mission The Lancers

class Warrior():

	attack = 5
	health = 50
	full_health = 50
	is_alive = True
	defence = 0

	def make_attack(self, defender, next_unit_attacker = None, next_unit_defender = None):
		attack = self.apply_defence(defender)
		defender.take_damage(attack)
		print(f'{self.__class__.__name__} does {attack} to {defender.__class__.__name__}, ending health {defender.health}')
		if isinstance(self, Vampire):
			self.bloodsuck(defender)
		if isinstance(self, Lancer):
			if next_unit_defender:
				self.piercing_attack(next_unit_defender)
		if next_unit_attacker and isinstance(next_unit_attacker, Healer):
			next_unit_attacker.heal(self)
		if defender.health <= 0:
			defender.is_alive = False
			return defender.is_alive
		return defender.health


	def apply_defence(self, defender):
		attack = max(0, self.attack - defender.defence)
		return attack

	def take_damage(self, damage):
		self.health -= damage

class Knight(Warrior):

	def __init__(self):
		super().__init__()

	attack = 7

class Defender(Warrior):
	
	def __init__(self):
		super().__init__()

	health = 60
	full_health = 60
	attack = 3
	defence = 2

class Rookie(Warrior):

	def __init__(self):
		super().__init__()

	attack = 1

class Vampire(Warrior):

	def __init__(self):
		super().__init__()

	health = 40
	full_health = 40
	attack = 4
	vampirism = 50

	def bloodsuck(self, defender):
		attack = self.apply_defence(defender)
		if not self.health + int((self.vampirism * attack / 100)) >= self.full_health:
			self.take_damage(-int((self.vampirism * attack / 100)))
			print(f'{self.__class__.__name__} sucked {int((self.vampirism * attack / 100))} from {defender.__class__.__name__} Vampire health is now {self.health}')

class Lancer(Warrior):

	def __init__(self):
		super().__init__()

	attack = 6
	piercing = 0.5

	def piercing_attack(self, next_unit_defender):
		piercing_damage = int(max(0, (self.attack * self.piercing) - next_unit_defender.defence))
		next_unit_defender.take_damage(piercing_damage)
		print(f'{self.__class__.__name__} pierced {next_unit_defender.__class__.__name__} for {piercing_damage} piercing damage, defender health now \
		{next_unit_defender.health}')

class Healer(Warrior):

	def __init__(self):
		super().__init__()

	attack = 0
	health = 60
	full_health = 60
	healing = 2

	def heal(self, unit_to_heal):
		print(f'{self.__class__.__name__} healed {unit_to_heal.__class__.__name__} to {unit_to_heal.health}')
		unit_to_heal.health = min(unit_to_heal.full_health, (unit_to_heal.health + self.healing))
		return unit_to_heal.health

class Army(list):

	def add_units(self, unit_type, no_of_units):
		for i in range(no_of_units): self.append(unit_type())
		return self

	def is_army_alive(self):
		return len(self) > 0

	def next_unit(self):
		return self[1] if len(self) > 1 else None

	def remove_dead(self):
		return self.pop(0)

class Battle():

	def fight(self, army_1, army_2):
		while army_1.is_army_alive() and army_2.is_army_alive():
			if fight(army_1[0], army_2[0], army_1.next_unit(), army_2.next_unit()):
				print(f' Army 2 Loses and loses {army_2[0].__class__.__name__}')
				army_2.remove_dead()
				
			else:
				print(f' Army 1 Loses and loses {army_1[0].__class__.__name__}')
				army_1.remove_dead()
		else:
			return army_1.is_army_alive()

def fight(unit_1, unit_2, unit_3 = None, unit_4 = None):

	print(f'Fight between {unit_1.__class__.__name__} and {unit_2.__class__.__name__}, with {unit_3.__class__.__name__} and {unit_4.__class__.__name__}')
	while unit_1.is_alive and unit_2.is_alive: 
		unit_1.make_attack(unit_2, unit_3, unit_4)
		if unit_2.is_alive:
			unit_2.make_attack(unit_1, unit_4, unit_3)
	return unit_1.is_alive

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
	eric = Vampire()
	adam = Vampire()
	richard = Defender()
	ogre = Warrior()
	freelancer = Lancer()
	vampire = Vampire()
	priest = Healer()

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
	assert fight(eric, richard) == False
	assert fight(ogre, adam) == True
	assert fight(freelancer, vampire) == True
	assert freelancer.is_alive == True
	assert freelancer.health == 14    
	priest.heal(freelancer)
	assert freelancer.health == 16

		#battle tests
	my_army = Army()
	my_army.add_units(Defender, 2)
	my_army.add_units(Healer, 1)
	my_army.add_units(Vampire, 2)
	my_army.add_units(Lancer, 2)
	my_army.add_units(Healer, 1)
	my_army.add_units(Warrior, 1)
	
	enemy_army = Army()
	enemy_army.add_units(Warrior, 2)
	enemy_army.add_units(Lancer, 4)
	enemy_army.add_units(Healer, 1)
	enemy_army.add_units(Defender, 2)
	enemy_army.add_units(Vampire, 3)
	enemy_army.add_units(Healer, 1)

	army_3 = Army()
	army_3.add_units(Warrior, 1)
	army_3.add_units(Lancer, 1)
	army_3.add_units(Healer, 1)
	army_3.add_units(Defender, 2)

	army_4 = Army()
	army_4.add_units(Vampire, 3)
	army_4.add_units(Warrior, 1)
	army_4.add_units(Healer, 1)
	army_4.add_units(Lancer, 2)

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == False
	assert battle.fight(army_3, army_4) == True
	print("Coding complete? Let's try tests!")

	army_1 = Army()
	army_2 = Army()
	army_1.add_units(Defender, 5)
	army_1.add_units(Vampire, 6)
	army_1.add_units(Warrior, 7)
	army_2.add_units(Warrior, 6)
	army_2.add_units(Defender, 6)
	army_2.add_units(Vampire, 6)
	battle = Battle()
	assert battle.fight(army_1, army_2) == False
