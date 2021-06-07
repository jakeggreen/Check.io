"""In this mission you should add a new class Warlord(), which should be the subclass of the Warrior class and have the next characteristics:
health = 100
attack = 4
defense = 2

Also, when the Warlord is included in any of the armies, that particular army gets the new move_units() method which allows to rearrange the units of that army for the better battle result. The rearrangement is done not only before the battle, but during the battle too, each time the allied units die. The rules for the rearrangement are as follow:
If there are Lancers in the army, they should be placed in front of everyone else.
If there is a Healer in the army, he should be placed right after the first soldier to heal him during the fight. If the number of Healers is > 1, all of them should be placed right behind the first Healer.
If there are no more Lancers in the army, but there are other soldiers who can deal damage, they also should be placed in first position, and the Healer should stay in the 2nd row (if army still has Healers).
Warlord should always stay way in the back to look over the battle and rearrange the soldiers when it's needed.
Every army can have no more than 1 Warlord.
If the army doesn’t have a Warlord, it can’t use the move_units() method."""

log_print = False

class Warrior(object):

	attack = 5
	health = 50
	full_health = 50
	is_alive = True

	def make_attack(self, defender, next_unit_attacker = None, next_unit_defender = None):
		attack = self.apply_defence(defender)
		defender.take_damage(attack)
		if log_print:
			print(f'{self.__class__.__name__} does {attack} to {defender.__class__.__name__}, ending health {defender.health}')
		if hasattr(self, 'vampirism'):
			self.bloodsuck(defender)
		if hasattr(self, 'piercing'):
			if next_unit_defender:
				self.piercing_attack(next_unit_defender)
		if next_unit_attacker and hasattr(next_unit_attacker, 'heal_power'):
			next_unit_attacker.heal(self)
		if defender.health <= 0:
			defender.is_alive = False
			if log_print:
				print(f'{defender.__class__.__name__} loses the fight and dies! Status = {defender.is_alive}')
			return defender.is_alive
		return defender.health


	def apply_defence(self, defender):
		if not hasattr(defender, 'defence'):
			return self.attack
		attack = max(0, self.attack - defender.defence)
		return attack

	def take_damage(self, damage):
		self.health -= damage

	def equip_weapon(self, weapon_name):
		self.attack = self.attack + weapon_name.attack
		self.health = max(self.health + weapon_name.health, 0)
		self.full_health = max(self.full_health + weapon_name.health, 0)
		if hasattr(self, 'defence') and weapon_name.defence != None:
			self.defence = self.defence + weapon_name.defence
		if hasattr(self, 'vampirism') and weapon_name.vampirism != None:
			self.vampirism = self.vampirism + weapon_name.vampirism
		if hasattr(self, 'heal_power') and weapon_name.heal_power != None:
			self.heal_power = self.heal_power + weapon_name.heal_power

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
		if not self.health + int((self.vampirism * attack / 100)//1) >= self.full_health:
			self.take_damage(-int((self.vampirism * attack / 100)//1))
			if log_print:
				print(f'{self.__class__.__name__} sucked {int((self.vampirism * attack / 100)//1)} from {defender.__class__.__name__} Vampire health is now {self.health}')

class Lancer(Warrior):
	def __init__(self):
		super().__init__()

	attack = 6
	piercing = 0.5

	def piercing_attack(self, next_unit_defender):
		if hasattr(next_unit_defender, 'defence'):
			piercing_damage = int(max(0, (self.attack * self.piercing) - next_unit_defender.defence))
		piercing_damage = int(self.attack * self.piercing)
		next_unit_defender.take_damage(piercing_damage)
		if log_print:
			print(f'{self.__class__.__name__} pierced {next_unit_defender.__class__.__name__} for {piercing_damage} piercing damage, defender health now {next_unit_defender.health}')

class Healer(Warrior):
	def __init__(self):
		super().__init__()

	attack = 0
	health = 60
	full_health = 60
	heal_power = 2

	def heal(self, unit_to_heal):
		if log_print:
			print(f'{self.__class__.__name__} healed {unit_to_heal.__class__.__name__} to {unit_to_heal.health}')
		unit_to_heal.health = min(unit_to_heal.full_health, (unit_to_heal.health + self.heal_power))
		return unit_to_heal.health

class Warlord(Warrior):
	def __init__(self):
		super().__init__()

	attack = 4
	health = 100
	full_health = 100 
	defence = 2

class Weapon(object):
	def __init__(self, health, attack, defence, vampirism, heal_power):
		self.health = health
		self.attack = attack 
		self.defence = defence
		self.vampirism = vampirism
		self.heal_power = heal_power

class Sword(Weapon):
	def __init__(self):
		super().__init__(health = 5, attack = 2, defence = None, vampirism = None, heal_power = None)

class Shield(Weapon):
	def __init__(self):
		super().__init__(health = 20, attack = -1, defence = 2, vampirism = None, heal_power = None)

class GreatAxe(Weapon):
	def __init__(self):
		super().__init__(health = -15, attack = 5, defence = -2, vampirism = 10, heal_power = None)

class Katana(Weapon):
	def __init__(self):
		super().__init__(health = -20, attack = 6, defence = -5, vampirism = 50, heal_power = None)

class MagicWand(Weapon):
	def __init__(self):
		super().__init__(health = 30, attack = 3, defence = -2, vampirism = 10, heal_power = 3)

class Army():
	def __init__(self):
		self.units = []

	def add_units(self, unit_type, no_of_units):
		no_of_units = 1 if unit_type == Warlord and no_of_units > 1 else no_of_units
		if log_print:
			print(unit_type, no_of_units)
		for i in range(no_of_units): self.units.append(unit_type())

	def is_army_alive(self):
		return len(self.units) > 0

	def next_unit(self):
		return self.units[1] if len(self.units) > 1 else None

	def remove_dead(self):
		self.units[:] = [x for x in self.units if x.is_alive]
		if log_print:
			print(self.units)

	def move_units(self):
		if any([x for x in self.units if x.__class__.__name__ == 'Lancer']):
			self.units.sort(key = lambda x: (hasattr(x, 'piercing'), hasattr(x, 'heal_power'), not isinstance(x, Warlord)), reverse = True)
		else:
			self.units.sort(key = lambda x: ((hasattr(x, 'attack') and x.attack > 0 and not isinstance(x, Warlord)), hasattr(x, 'heal_power')), reverse = True)

		# 	number_of_healers = len([x for x in self.units if x.__class__.__name__ == 'Healer'])
		# print(number_of_healers)
		#lancers at the front, healer behind them, all other healers next, then fighters behind them and warlords at the back

		
class Battle():

	def fight(self, army_1, army_2):
		while army_1.is_army_alive() and army_2.is_army_alive():
			if fight(army_1.units[0], army_2.units[0], army_1.next_unit(), army_2.next_unit()):
				if log_print:
					print(f' Army 2 Loses and loses {army_2[0].__class__.__name__}')
				army_2.remove_dead()
			else:
				if log_print:
					print(f' Army 1 Loses and loses {army_1[0].__class__.__name__}')
				army_1.remove_dead()
		else:
			return army_1.is_army_alive()

	def straight_fight(self, army_1, army_2):
		#take first soldier from army_1 and first from army_2 and fight - continue for all soldiers in each army
		#once fights have done, remove the dead soldiers and repeat until winner
		while army_1.is_army_alive() and army_2.is_army_alive():
			size_of_army = max(len(army_1.units), len(army_2.units))
			for x in range(0, size_of_army):
				try:
					fight(army_1.units[x], army_2.units[x])
				except Exception:
					pass		
			army_1.remove_dead()
			army_2.remove_dead()
		else:
			return army_1.is_army_alive()

def fight(unit_1 = None, unit_2 = None, unit_3 = None, unit_4 = None):

	if not unit_2:
		return unit_1.is_alive
	if not unit_1:
		return unit_2.is_alive
	if log_print:
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

	army_5 = Army()
	army_5.add_units(Warrior, 10)

	army_6 = Army()
	army_6.add_units(Warrior, 6)
	army_6.add_units(Lancer, 5)

	battle = Battle()

	army_1 = Army()

	army_1.add_units(Lancer, 7)
	army_1.add_units(Vampire, 3)
	army_1.add_units(Warrior, 4)
	army_1.add_units(Defender, 2)

	army_2 = Army()
	army_2.add_units(Warrior, 4)
	army_2.add_units(Defender, 4)
	army_2.add_units(Vampire, 6)
	army_2.add_units(Lancer, 4)

	assert battle.straight_fight(army_1, army_2) == True
	assert battle.fight(my_army, enemy_army) == False
	assert battle.fight(army_3, army_4) == True
	assert battle.straight_fight(army_5, army_6) == False
	print("Coding complete? Let's try tests!")

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	
	ogre = Warrior()
	lancelot = Knight()
	richard = Defender()
	eric = Vampire()
	freelancer = Lancer()
	priest = Healer()

	sword = Sword()
	shield = Shield()
	axe = GreatAxe()
	katana = Katana()
	wand = MagicWand()
	super_weapon = Weapon(50, 10, 5, 150, 8)

	ogre.equip_weapon(sword)
	ogre.equip_weapon(shield)
	ogre.equip_weapon(super_weapon)
	lancelot.equip_weapon(super_weapon)
	richard.equip_weapon(shield)
	eric.equip_weapon(super_weapon)
	freelancer.equip_weapon(axe)
	freelancer.equip_weapon(katana)
	priest.equip_weapon(wand)
	priest.equip_weapon(shield)

	ogre.health == 125
	lancelot.attack == 17
	richard.defence == 4
	eric.vampirism == 200
	freelancer.health == 15
	priest.heal_power == 5

	fight(ogre, eric) == False
	fight(priest, richard) == False
	fight(lancelot, freelancer) == True

	my_army = Army()
	my_army.add_units(Knight, 1)
	my_army.add_units(Lancer, 1)

	enemy_army = Army()
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 1)

	my_army.units[0].equip_weapon(axe)
	my_army.units[1].equip_weapon(super_weapon)

	enemy_army.units[0].equip_weapon(katana)
	enemy_army.units[1].equip_weapon(wand)

	battle = Battle()

	battle.fight(my_army, enemy_army) == True
	print("Coding complete? Let's try tests!")

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	
	ronald = Warlord()
	heimdall = Knight()

	assert fight(heimdall, ronald) == False

	my_army = Army()
	my_army.add_units(Warlord, 1)
	my_army.add_units(Warrior, 2)
	my_army.add_units(Lancer, 2)
	my_army.add_units(Healer, 2)

	enemy_army = Army()
	enemy_army.add_units(Warlord, 3)
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 2)
	enemy_army.add_units(Knight, 2)

	my_army.move_units()
	enemy_army.move_units()

	print(my_army.units)
	print(enemy_army.units)

	assert type(my_army.units[0]) == Lancer
	assert type(my_army.units[1]) == Healer
	assert type(my_army.units[-1]) == Warlord

	assert type(enemy_army.units[0]) == Vampire
	assert type(enemy_army.units[-1]) == Warlord
	assert type(enemy_army.units[-2]) == Knight

	#6, not 8, because only 1 Warlord per army could be
	assert len(enemy_army.units) == 6

	battle = Battle()

	assert battle.fight(my_army, enemy_army) == True
	print("Coding complete? Let's try tests!")