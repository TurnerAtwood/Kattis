"""
/*	Turner Atwood
 *	11/3/19
 *	Perket [2.2] https://open.kattis.com/problems/perket 
 *	Ad-hoc : Trivial math
 */
"""

from itertools import combinations
from math import inf

def main():
	N = int(input())
	ings = list()
	for i in range(N):
		ings.append(tuple(int(i) for i in input().split()))

	best = inf
	for size in range(1,N+1):
		# Gen all permutations
		for perm in combinations(ings,size):
			sour = 1
			bitter = 0
			for ing in list(perm):
				sour *= ing[0]
				bitter += ing[1]
			best = min(best, abs(sour - bitter))
	print(best)

if __name__ == "__main__":
	main()