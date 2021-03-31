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
# 	return sum((max(start_watching or end, end) - max(start_watching or start, start)).total_seconds() for start, end in zip(els[::2], els[1::2]))

from datetime import datetime
from typing import List, Optional

#method 1 - doesn't work where the start and end are inbetween two existing on/off times

# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:

# 	starts = list(els[::2])
# 	ends = list(els[1::2])

# 	if start_watching == els[-1]: return 0

# 	try:
# 		min_start = min(start for start in starts if start > start_watching)
# 	except Exception:
# 		min_start = start_watching
# 	try:
# 		min_end = min(end for end in ends if end < end_watching)
# 	except Exception:
# 		min_end = end_watching

# 	print("start: " + str(min_start), "end: " + str(min_end))
# 	print("start: " + str(min(min_start, start_watching)), "end: " + str(min(min_end, end_watching)))

# 	return (min(min_end, end_watching) - min(min_start, start_watching)).total_seconds() if min_start < min_end or min(min_start, start_watching) < min(min_end, end_watching) else 0

#method 2 - taking each pair, check start against the off time

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None) -> int:

	seconds = 0

	if len(els) %2 != 0: # if the length of els is odd then it ends with light switch being on, so adding in end watching to get equal number of pairs
		els.append(end_watching) 

	for pair in zip(els[::2],els[1::2]):

		# print(pair[0],pair[-1])

		if not start_watching > pair[-1] and end_watching > pair[0]: # start after pair

			if start_watching <= pair[0] and end_watching >= pair[-1]: #whole pair included
				seconds += (pair[0] - pair[-1]).total_seconds()

			if start_watching <= pair[0] and end_watching < pair[-1]: #start before pair, but end during pair
				seconds += (pair[0] - end_watching).total_seconds()

			if start_watching > pair[0] and end_watching <= pair[-1]:
				seconds += (start_watching - end_watching).total_seconds() #start and end inside of the pair

			if start_watching >= pair[0] and end_watching > pair[-1]: #start at beginning of pair, end after		
				seconds += (start_watching - pair[-1]).total_seconds()

		seconds += 0

	# print(abs(seconds))

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