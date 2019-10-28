"""
/*	Turner Atwood
 *	10/27/19
 *	Shuffling Along [2.9] https://open.kattis.com/problems/shuffling
 *	Ad-hoc : Generate permutation and brute-force
 */
"""
from math import ceil

def apply(deck, perm):
	out = [0 for i in deck]
	for i in range(len(perm)):
		out[i] = deck[perm[i]]

	return out

def main():
	line = input().split()
	N = int(line[0])
	out = line[1] == "out"

	deck = [i for i in range(N)]
	start = [i for i in range(N)]
	perm = list()

	half = ceil(N/2)
	for i in range(N//2):
		if out:
			perm.append(i)
			perm.append(i+half)
		else:
			if N%2 == 1:
				perm.append(i+half-1)
			else:
				perm.append(i+half)
			perm.append(i)
	if N%2 == 1:
		if out:
			perm.append(N//2)
		else:
			perm.append(N-1)


	count = 1
	deck = apply(deck,perm)

	while(deck != start):
		count += 1
		deck = apply(deck,perm)
	print(count)

if __name__ == "__main__":
	main()