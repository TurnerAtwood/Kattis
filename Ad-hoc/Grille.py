"""
/*	Turner Atwood
 *	10/31/19
 *	Grille [3.6] https://open.kattis.com/problems/grille
 *	Ad-hoc : Messy matrix manipulation/rotation
 */
"""

from collections import deque

def rotate(N, grille):
	out1 = [[0 for j in range(N)] for i in range(N)]
	out2 = [[0 for j in range(N)] for i in range(N)]
	# Flip accross main diag
	for i in range(N):
		for j in range(N):
			out1[i][j] = grille[j][i]
	# Flip accross Y-axis
	for i in range(N):
		for j in range(N):
			out2[i][j] = out1[i][N-1-j]
	return out2

def covered(N, grille):
	res = list()
	for i in range(N):
		for j in range(N):
			if (grille[i][j] == 1):
				res.append((i,j))
	return res

def main():
	# Input
	N = int(input())
	grille = [[1 if i=="." else 0 for i in input() ]	for j in range(N)]
	secret = deque([i for i in input()])
	
	# Grab the spots to put letters back into the grid
	spots = list()
	for i in range(4):
		spots += covered(N, grille)
		grille = rotate(N, grille)

	# Try to put the letters back into the grid for all
	##	spots found. Failure implies a bad grille
	out = [[0 for j in range(N)] for i in range(N)]
	try:
		for i,j in spots:
			out[i][j] = secret.popleft()
		return "".join(["".join(i) for i in out])
	except:
		return "invalid grille"

if __name__ == "__main__":
	print(main())