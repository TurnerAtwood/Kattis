"""
/*	Turner Atwood
 *	12/15/19
 *	Kitchen Measurements [3.5] https://open.kattis.com/problems/kitchen
 *	Dijsktra's - Try states with smallest pours first
 *	Takes a few seconds to run (time limit 10 seconds)
 */
"""

import heapq
from copy import deepcopy

def main():
	# Input
	sizes = [int(i) for i in input().split()]
	target = sizes.pop()
	n = sizes.pop(0)
	sizes.sort(reverse=True)

	# cur_cups stores the current state of the cups
	cur_cups = [sizes[0]] + [0]*(n-1)

	# This will be a pq (heap)
	pq = [(0,tuple(cur_cups))]
	visited = dict()

	# Dijkstra's Algorithm (I guess)
	while pq:
		d,cur_cups_orig = heapq.heappop(pq)
		# Early exit
		if cur_cups_orig[0] == target:
			return d

		# No need to repeat
		if cur_cups_orig in visited:
			continue

		visited[cur_cups_orig] = d

		for i in range(n):
			if not cur_cups[i]:
				continue
			# Try to pour from i -> j
			for j in range(n):
				cur_cups = list(deepcopy(cur_cups_orig))
				
				# Cannot pour into a full cup or self
				if j == i or cur_cups[j] == sizes[j]:
					continue
				# j is filled
				cur_cups[j] += cur_cups[i] 
				if cur_cups[j] > sizes[j]:
					cur_cups[i] = cur_cups[j] - sizes[j]
					cur_cups[j] = sizes[j]
				# i can be emptied into j
				else:
					cur_cups[i] = 0

				# Put the new state on the priority queue
				cur_cups = tuple(cur_cups)
				poured = cur_cups_orig[i] - cur_cups[i]
				if cur_cups not in visited:
					heapq.heappush(pq, (d + poured, cur_cups))

	return "impossible"

if __name__ == "__main__":
	print(main())