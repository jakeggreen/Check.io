"""In the previous mission, the start_watching parameter was introduced, and in this one - the end_watching parameter, which tells the time when it’s necessary to end the observation. If it’s not passed, the mission works as in the previous version, with no observation time limit.

One more update is that the amount of elements (button clicks) can be odd (previously there was a precondition, that the amount of elements is always even).

example

Input: Three arguments and only the first one is required. The first one is a list of datetime objects, the second and the third ones are the datetime objects.

Output: A number of seconds as an integer."""

# def sum_light(els: List[datetime]) -> int:
# 	button_pairs = [els[i:i+2] for i in range(0,len(els),2)]
# 	seconds = 0
# 	for pair in button_pairs:
# 		seconds += abs(pair[1] - pair[0]).total_seconds()
# 	return int(seconds)

# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
# 	if start_watching:
# 		new_els = []
# 		[new_els.append(date) for date in els if date > start_watching and start_watching] 			
# 		new_els.append(start_watching) 																
# 		new_els = sorted(new_els, key=None, reverse=False)											
# 		if len(new_els) == 1:																		
# 			return 0
# 		els = new_els																				
# 	button_pairs = [els[i:i+2] for i in range(0,len(els),2)]										
# 	seconds = 0 																					
# 	for pair in button_pairs:																	
# 		seconds += abs(pair[1] - pair[0]).total_seconds()										
# 	return int(seconds) 

from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:
	if start_watching or end_watching:
		if end_watching > els[-1]:
			return 0
		els = []
		[els.append(date) for date in els if date <= start_watching or date > end_watching] 
		try:
			els.append(start_watching) if start_watching < els[0] else None, els.append(end_watching) if end_watching >= els[-1] else None
		except:
			els.append(start_watching), els.append(end_watching)
		els = sorted(els, key=None, reverse=False)											
		if len(els) == 1:																		
			return 0
		print(els)
	button_pairs = [els[i:i+2] for i in range(0,len(els),2)]
	print(button_pairs)										
	seconds = 0 																					
	for pair in button_pairs:																	
		seconds += abs(pair[1] - pair[0]).total_seconds()										
	return int(seconds) 

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