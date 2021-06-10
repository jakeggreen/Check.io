"""As the input you will get the chemical formula and the number N. Your task is to create a list of the chemical elements, which are in the formula in the amount of >= N.
Pay attention, that in the some formulas will be used brackets - () and []. This article will help you to open the brackets and don't make mistake while counting.

Input: Chemical formula and the number of atoms.

Output: List of the chemical elements, sorted in the alphabetical order."""

import re

def rec(formula, multiplier):

	elements = {}

	#need to deal with anything outside of the brackets

	outside_brackets = re.findall(r'([A-Z][a-z]*)(\d*)[\(\[]\S+[\)\]]\d*', formula)
	
	if outside_brackets:
		for each in outside_brackets:
			z = 1 if each[1] == '' else int(each[1])
			elements.update({each[0]: m + (z * multiplier)}) if (m := elements.get(each[0])) else elements.update({each[0]: z})

	brackets = re.findall(r'[\(\[](\S+)[\)\]](\d*)', formula)

	if brackets:
		for item in brackets:
			j = 1 if item[1] == '' else int(item[1])
			for y in rec(item[0], j * multiplier):
				elements.update({y: s + (j * multiplier)}) if (s := elements.get(y)) else elements.update({y: j})
	else:
		arr = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
		for x in arr:
			i = 1 if x[1] == '' else int(x[1])
			elements.update({x[0]: s + (i * multiplier)}) if (s := elements.get(x[0])) else elements.update({x[0]: i})
	
	print(elements)
	
	return elements

def atoms(formula, limit):

	elements = rec(formula, 1)

	ordered_list = sorted([item for item in elements if elements.get(item) >= limit], reverse = False)

	print(ordered_list)

	return ordered_list

if __name__ == '__main__':
	print("Example:")
	print(atoms('C2H5OH', 2))

	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert atoms('C2H5OH2', 2) == ['C', 'H']
	assert atoms('H2O', 2) == ['H']
	assert atoms('Mg(OH)2', 1) == ['H', 'Mg', 'O']
	assert atoms('K4[ON(SO3)2]2', 4) == ['K', 'O', 'S']
	print("Coding complete? Click 'Check' to earn cool rewards!")
