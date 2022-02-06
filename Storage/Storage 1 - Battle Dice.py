"""For this task, you need to figure out what your probability of winning a board game is. The game involves two players moving units around a map. When the units battle and both players roll several dice, one for each unit, to see who wins and at what cost. You want to find the probability of winning one of these battles, regardless of any losses. Keep in mind that if the battle ends with no units remaining on either side, that's a draw, not a win.

When a conflict begins, each player rolls one die per unit. Each die has a number of attack icons and defense icons on each side. After a roll, the player loses a number of units equal to the number of attack icons the opponent rolled minus the number of defense icons they rolled themselves. For example, if player one rolled 2 attack icons and 4 defense icons and player two rolled 3 attack icons and 1 defense icons, player one would lose 0 units (3 - 4 but you can't lose negative units) and player two would lose 1 unit (2 - 1).

After unit losses are applied, the players roll again. This continues until one player has no units remaining.

You are given a description of the dice as a list of which icons are on a face and how many dice each player has. All of the dice are exactly the same. Each element in the list is a string containing zero or more A's representing the attack icons and zero or more D's representing the defense icons. (A face can be blank.) For example, the list ["AAD", "ADD", "A", "D", "", ""] represents a six sided die with two attack and one defense on one face, one attack and two defense on another, a single attack on the third face, a single defense on the fourth and two blank faces.

You should calculate the probability that player one will win the conflict. If player one has a 1 in 7 chance of winning, you should return ≈0.1429. The result should be given with four digits precision as ±0.0001.

Input: Three arguments. A dice description as a list of strings. A number of units for player one and player two as integers.

Output: The probability that player one will win the conflict as a float or integer."""

from itertools import product

win_count = 0

def attack(attacker, defender, units):
	attack = attacker.count('A') - defender.count('D') if attacker.count('A') - defender.count('D') >= 0 else 0
	outcome = (units - attack) if (units - attack) >= 0 else 0
	return outcome

def player_options(dice_description, units):
	K = units
	temp = [dice_description for _ in range(K)]
	return list(product(*temp))

def create_roll_lists(dice_list, units):
	x = [a.split() for a in [''.join(a) for a in player_options(dice_list, units)]]
	x = [[a for b in c for a in b] for c in x]
	return x

def skirmish():
	pass

def battle_probability(dice_description, units_one, units_two):

	player_one = create_roll_lists(dice_description, units_one)
	player_two = create_roll_lists(dice_description, units_two)

	outcomes = {}
	perms = 0

	for one_dice_roll in player_one:
		for two_dice_roll in player_two:
			one_outcome = attack(two_dice_roll, one_dice_roll, units_one)
			two_outcome = attack(one_dice_roll, two_dice_roll, units_two)
			if not outcomes.get((one_outcome, two_outcome)):
				outcomes[(one_outcome, two_outcome)] = 1
			else:
				outcomes[(one_outcome, two_outcome)] += 1
			perms += 1

	print(f'Given the {perms} iterations, the outcomes are: {outcomes}')

	win_count = 0

	for key in outcomes:
		if key[0] > key[1]:
			win_count += outcomes.get(key)

	win_prob = win_count/perms

	print(f'This means that one wins {win_count} games, with a probability of {win_prob}')

	return win_prob

if __name__ == '__main__':
	#These are only used for self-checking and are not necessary for auto-testing
	def almost_equal(checked, correct, significant_digits=4):
		precision = 0.1 ** significant_digits
		return correct - precision < checked < correct + precision

	assert(almost_equal(battle_probability(['A', 'D'], 3, 3), 0.0000)), "Always ties, nobody wins"
	assert(almost_equal(battle_probability(['A', 'D'], 4, 3), 1.0000)), "Always win"
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 3, 4), 0.0186)), "You can win"
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 4, 4), 0.4079)), "Ready to fight"
	assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 5, 4), 0.9073)), "I have good chance"
