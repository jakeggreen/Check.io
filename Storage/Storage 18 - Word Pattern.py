"""Sophia's drones are too simple and can recognize symbols in only single words, digits or letters. She wants to teach the drones to understand basic commands which are represented as "words" consisted by letters and digits. For that, Sophia has uploaded "patterns," which describe the sequence of digits and letters in the command. Unfortunately, the drones memory can only store integers and convert them into binary format for comparison. We should help Sophia to write a module for the comparison of patterns and commands.

You are given a pattern as a positive integer and a command as a word. For the comparison, the drone should convert the integer pattern into binary form, append zeros to left for the command length and compare this combination with the command.
1 is a letter. 0 is a digit.
If the pattern and the command are coincided, then return True, else -- False. If pattern is longer than a command, then they are not coincided (For example - 8 = 1000 and "a")."""

import re

def convert_to_binary(pattern, padding):
	binary = "{0:b}".format(pattern)
	if len(binary) > padding:
		return False
	else:
		padded_binary = '0' * (padding-len(binary)) + binary
	return padded_binary

def convert_command(command):
	return re.sub('[a-zA-z]', '1', re.sub('[0-9]', '0', command))

def check_command(pattern, command):
    binary = convert_to_binary(pattern, len(command))
    command = convert_command(command)
    return True if binary == command else False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_command(42, "12a0b3e4") == True, "42 is the answer"
    assert check_command(101, "ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, "478103487120470129") == True, "Any number"
    assert check_command(127, "Checkio") == True, "Uppercase"
    assert check_command(7, "Hello") == False, "Only full match"
    assert check_command(8, "a") == False, "Too short command"
    assert check_command(5, "H2O") == True, "Water"
    assert check_command(42, "C2H5OH") == False, "Yep, this is not the Answer"

