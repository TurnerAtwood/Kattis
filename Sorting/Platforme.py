"""
/*	Turner Atwood
 *	11/3/19
 *	Platforme [2.6] https://open.kattis.com/problems/platforme
 *	Sorting : Sort by starts and endpoints then linear scan
 */
"""
from collections import deque

def findUnder(array, val):
	lowest = 0
	for item in array:
		if item < val and item > lowest:
			lowest = item
	return lowest

def main():
	N = int(input())

	starts = list()
	ends = list()
	for i in range(N):
		plat = tuple([int(i) for i in input().split()])
		starts.append((plat[1],plat[0]))
		ends.append((plat[2],plat[0]*-1))
	starts.sort(reverse=True)
	ends.sort(reverse=True)
	
	# Find the smallest on the end of starts or ends
	cost = 0
	cur_heights = list()
	while (ends):
		# Do some special stuff once start is empty

		# Adding a new platform
		if (starts and starts[-1][0] < ends[-1][0]):
			plat = starts.pop()
			cost += plat[1] - findUnder(cur_heights, plat[1])
			cur_heights.append(plat[1])
		# Removing a platform
		else:
			plat = ends.pop()
			cost += plat[1]*-1 - findUnder(cur_heights, plat[1]*-1)
			cur_heights.remove(plat[1]*-1)
	print(cost)


if __name__ == "__main__":
	main()