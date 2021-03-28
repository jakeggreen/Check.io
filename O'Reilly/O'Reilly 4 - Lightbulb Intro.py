"""With this mission I want to start a series of missions with light bulbs. They will help you understand the concept of processes and evaluation of the processes’ performance. Instead of light bulbs, in real life, there may be equipment, the effectiveness of which must be calculated, or workers who go to work, and their wages must be calculated.

The first mission is quite simple. There is a light bulb, which by default is off, and a button, by pressing which the light bulb switches its state. This means that if the light bulb is off and the button is pressed, the light turns on, and if you press it again, it turns off.

(Everything is easy. I am sure that if you’ve got to this mission, you should understand, but just in case I’m adding a visual.)

example

The function input is an array of datetime objects - this is the date and time of pressing the button. Your task is to determine how long the light bulb has been turned on.

Input: A list of datetime objects

Output: A number of seconds as an integer."""

from datetime import datetime
from typing import List

def sum_light(els: List[datetime]) -> int:
	button_pairs = [els[i:i+2] for i in range(0,len(els),2)]
	seconds = 0
	for pair in button_pairs:
		seconds += abs(pair[1] - pair[0]).total_seconds()
	return int(seconds)

if __name__ == '__main__':
	print("Example:")
	print(sum_light([
		datetime(2015, 1, 12, 10, 0 , 0),
		datetime(2015, 1, 12, 10, 10 , 10),
		datetime(2015, 1, 12, 11, 0 , 0),
		datetime(2015, 1, 12, 11, 10 , 10),
	]))
	
	# These "asserts" are used for self-checking and not for an auto-testing
	assert sum_light([
		datetime(2015, 1, 12, 10, 0 , 0),
		datetime(2015, 1, 12, 10, 10 , 10),
	]) == 610

	assert sum_light([
		datetime(2015, 1, 12, 10, 0 , 0),
		datetime(2015, 1, 12, 10, 10 , 10),
		datetime(2015, 1, 12, 11, 0 , 0),
		datetime(2015, 1, 12, 11, 10 , 10),
	]) == 1220

	assert sum_light([
		datetime(2015, 1, 12, 10, 0 , 0),
		datetime(2015, 1, 12, 10, 10 , 10),
		datetime(2015, 1, 12, 11, 0 , 0),
		datetime(2015, 1, 12, 11, 10 , 10),
		datetime(2015, 1, 12, 11, 10 , 10),
		datetime(2015, 1, 12, 12, 10 , 10),
	]) == 4820

	assert sum_light([
		datetime(2015, 1, 12, 10, 0 , 0),
		datetime(2015, 1, 12, 10, 0 , 1),
	]) == 1

	assert sum_light([
		datetime(2015, 1, 12, 10, 0 , 0),
		datetime(2015, 1, 12, 10, 0 , 10),
		datetime(2015, 1, 12, 11, 0 , 0),
		datetime(2015, 1, 13, 11, 0 , 0),
	]) == 86410

	print("The first mission in series is completed? Click 'Check' to earn cool rewards!")