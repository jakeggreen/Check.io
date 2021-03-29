"""This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.

You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. Now let's add one more parameter - the counting start time.

This means that the light continues to turn on and off as before. But now, as a result of the function, I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.

One more argument is added – start_watching , and if it’s not passed, we count as in the previous version of the program for the entire period.

Input: Two arguments and only the first one is required. The first one is a list of datetime objects and the second one is a datetime object.

Output: A number of seconds as an integer."""

from datetime import datetime, date, time
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
	new_els = []
	if start_watching:																				#check is the optional start watching datetime is populated
		[new_els.append(date) for date in els if date > start_watching] 							#remove all dates before or equal to the datetime started watching
		new_els.append(start_watching) 																#add in the start watching date
		new_els = sorted(new_els, key=None, reverse=False)											#re-sort the list
		if len(new_els) == 1:																		#check for only one datetime 
			return 0																				#if there's only one datetime return 0
		els = new_els																				#set the old list equal to the new one
	button_pairs = [els[i:i+2] for i in range(0,len(els),2)]										#split into pairs of dates
	seconds = 0 																					#set seconds equal to zero
	for pair in button_pairs:																		#loop through the pairs
		seconds += abs(pair[1] - pair[0]).total_seconds()											#find difference between each pair in seconds and add to total
	return int(seconds) 																			#return the seconds as an int instead of float

if __name__ == '__main__':
	print("Example:")
	print(sum_light([
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 10, 10),
datetime(2015, 1, 12, 11, 0, 0),
datetime(2015, 1, 12, 11, 10, 10)
]))
	
	assert sum_light(els=[
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
	start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	], datetime(2015, 1, 12, 10, 0, 0)) == 10
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	], datetime(2015, 1, 12, 11, 0, 0)) == 610
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	], datetime(2015, 1, 12, 11, 0, 10)) == 600
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	], datetime(2015, 1, 12, 10, 10, 0)) == 620

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
		datetime(2015, 1, 12, 11, 10, 11),
		datetime(2015, 1, 12, 12, 10, 11),
	], datetime(2015, 1, 12, 12, 10, 11)) == 0

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
		datetime(2015, 1, 12, 11, 10, 11),
		datetime(2015, 1, 12, 12, 10, 11),
	], datetime(2015, 1, 12, 12, 9, 11)) == 60
	
	print("The second mission in series is done? Click 'Check' to earn cool rewards!")