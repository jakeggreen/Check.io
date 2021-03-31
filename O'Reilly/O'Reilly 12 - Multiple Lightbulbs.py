"""In the 4th mission of the series more light bulbs are added.

You still must determine how long the room will be lit during the observation period between start_watching and end_watching. But now we have more than one light bulb. This means that in the light bulb switching array can now also be passed the number of the light bulb, the button of which is being pressed.

Each element of the button clicking array can be either a datetime object (which means the time when the first button was pressed) or a tuple of 2 elements (where the first elements is a datetime object, the time the button was pressed), and the second is the number of the light bulb, the button of which is being pressed.

If the passed array will only consist of datetime elements, then we have only one light bulb and the function should work the same way as in the previous mission of the series.

example

Input: Three arguments and only the first one is required. The first one is a list of datetime objects (instead of datetime object there can be a tuple of two datetime and int), the second and the third ones are the datetime objects.

Output: A number of seconds as an integer."""

# Taken from mission Lightbulb End Watching

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:

	seconds = 0

	if len(els) %2 != 0: #if the length of els is odd then it ends with light switch being on, so adding in end watching to get equal number of pairs
		els.append(end_watching)

	if end_watching == None: end_watching = datetime(9999, 12, 31, 23, 59, 59)
	if start_watching == None: start_watching = datetime(1900, 1, 12, 10, 0, 0)

	for pair in zip(els[::2],els[1::2]):

		if not start_watching > pair[-1] and end_watching > pair[0]: # start after pair

			if start_watching <= pair[0] and end_watching >= pair[-1]: #whole pair included
				seconds += (pair[0] - pair[-1]).total_seconds()

			if start_watching <= pair[0] and end_watching < pair[-1]: #start before pair, but end during pair
				seconds += (pair[0] - end_watching).total_seconds()

			if start_watching > pair[0] and end_watching <= pair[-1]:
				seconds += (start_watching - end_watching).total_seconds() #start and end inside of the pair

			if start_watching > pair[0] and end_watching > pair[-1]: #start at beginning of pair, end after		
				seconds += (start_watching - pair[-1]).total_seconds()
		else:

			seconds += 0

	return int(abs(seconds))

	return int(abs(seconds))



if __name__ == '__main__':
	print("Example:")
	print(sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
	datetime(2015, 1, 12, 10, 0, 0),
	datetime(2015, 1, 12, 10, 0, 10)))
	
	assert sum_light(els=[
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
	start_watching=datetime(2015, 1, 12, 10, 0, 0),
	end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
	datetime(2015, 1, 12, 10, 0, 0),
	datetime(2015, 1, 12, 10, 0, 7)) == 7
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
	datetime(2015, 1, 12, 10, 0, 3),
	datetime(2015, 1, 12, 10, 0, 10)) == 7
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
	],
	datetime(2015, 1, 12, 10, 0, 10),
	datetime(2015, 1, 12, 10, 0, 20)) == 0
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
	datetime(2015, 1, 12, 10, 30, 0),
	datetime(2015, 1, 12, 11, 0, 0)) == 0
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
	datetime(2015, 1, 12, 10, 10, 0),
	datetime(2015, 1, 12, 11, 0, 0)) == 10
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
	datetime(2015, 1, 12, 10, 10, 0),
	datetime(2015, 1, 12, 11, 0, 10)) == 20
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
	datetime(2015, 1, 12, 9, 50, 0),
	datetime(2015, 1, 12, 10, 0, 10)) == 10
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
	datetime(2015, 1, 12, 9, 0, 0),
	datetime(2015, 1, 12, 10, 5, 0)) == 300
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
		datetime(2015, 1, 12, 11, 10, 10),
	],
	datetime(2015, 1, 12, 11, 5, 0),
	datetime(2015, 1, 12, 12, 0, 0)) == 310
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
	],
	datetime(2015, 1, 12, 11, 5, 0),
	datetime(2015, 1, 12, 11, 10, 0)) == 300
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
	],
	datetime(2015, 1, 12, 10, 10, 0),
	datetime(2015, 1, 12, 11, 0, 10)) == 20
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 10, 10),
		datetime(2015, 1, 12, 11, 0, 0),
	],
	datetime(2015, 1, 12, 9, 10, 0),
	datetime(2015, 1, 12, 10, 20, 20)) == 610
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
	],
	datetime(2015, 1, 12, 9, 10, 0),
	datetime(2015, 1, 12, 10, 20, 20)) == 1220
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
	],
	datetime(2015, 1, 12, 9, 9, 0),
	datetime(2015, 1, 12, 10, 0, 0)) == 0
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
	],
	datetime(2015, 1, 12, 9, 9, 0),
	datetime(2015, 1, 12, 10, 0, 10)) == 10
	
	print("The third mission in series is completed? Click 'Check' to earn cool rewards!")

from datetime import datetime
from typing import List, Optional, Union, Tuple

def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
		start_watching: Optional[datetime] = None,
		end_watching: Optional[datetime] = None) -> int:
	"""
		how long the light bulb has been turned on
	"""
	return 0


if __name__ == '__main__':
	print("Example:")

	print(sum_light(els=[
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], start_watching=datetime(2015, 1, 12, 10, 0, 0), end_watching=datetime(2015, 1, 12, 10, 1, 0)))

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		(datetime(2015, 1, 12, 10, 0, 0), 2),
		datetime(2015, 1, 12, 10, 0, 10),
		(datetime(2015, 1, 12, 10, 1, 0), 2),
	]) == 60

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		datetime(2015, 1, 12, 10, 0, 10),
		(datetime(2015, 1, 12, 11, 0, 0), 2),
		(datetime(2015, 1, 12, 11, 1, 0), 2),
	]) == 70

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	]) == 30
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	]) == 40

	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
		(datetime(2015, 1, 12, 10, 1, 0), 3),
		(datetime(2015, 1, 12, 10, 1, 20), 3),
	]) == 60

	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		(datetime(2015, 1, 12, 10, 0, 0), 2),
		datetime(2015, 1, 12, 10, 0, 10),
		(datetime(2015, 1, 12, 10, 1, 0), 2),
	], datetime(2015, 1, 12, 10, 0, 50)) == 10
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 30)) == 20
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 20)) == 30
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 10)) == 30
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 50)) == 0
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 30)) == 20
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 20)) == 30
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
		(datetime(2015, 1, 12, 10, 1, 20), 2),
		(datetime(2015, 1, 12, 10, 1, 40), 2),
	], datetime(2015, 1, 12, 10, 0, 20)) == 50
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		(datetime(2015, 1, 12, 10, 0, 0), 2),
		datetime(2015, 1, 12, 10, 0, 10),
		(datetime(2015, 1, 12, 10, 1, 0), 2),
	], datetime(2015, 1, 12, 10, 0, 30), datetime(2015, 1, 12, 10, 1, 0)) == 30
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		(datetime(2015, 1, 12, 10, 0, 0), 2),
		datetime(2015, 1, 12, 10, 0, 10),
		(datetime(2015, 1, 12, 10, 1, 0), 2),
	], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40
	
	assert sum_light([
		datetime(2015, 1, 12, 10, 0, 0),
		(datetime(2015, 1, 12, 10, 0, 0), 2),
		datetime(2015, 1, 12, 10, 0, 10),
	], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30)) == 30
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0)) == 40
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)) == 0
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
		datetime(2015, 1, 12, 10, 0, 40),
		(datetime(2015, 1, 12, 10, 0, 50), 2),
	], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
	

	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
	], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
	
	assert sum_light([
		(datetime(2015, 1, 12, 10, 0, 10), 3),
		datetime(2015, 1, 12, 10, 0, 20),
		(datetime(2015, 1, 12, 10, 0, 30), 3),
		(datetime(2015, 1, 12, 10, 0, 30), 2),
	], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 30)) == 20    

	assert sum_light(els=[
		(datetime(2015, 1, 11, 0, 0, 0), 3),
		datetime(2015, 1, 12, 0, 0, 0),
		(datetime(2015, 1, 13, 0, 0, 0), 3),
		(datetime(2015, 1, 13, 0, 0, 0), 2),
		datetime(2015, 1, 14, 0, 0, 0),
		(datetime(2015, 1, 15, 0, 0, 0), 2),
	], start_watching=datetime(2015, 1, 10, 0, 0, 0), end_watching=datetime(2015, 1, 16, 0, 0, 0)) == 345600

	print("The forth mission in series is completed? Click 'Check' to earn cool rewards!")
