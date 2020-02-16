"""
/*	Turner Atwood
 *	1/29/20
 *	Keyboards in Concert [3.6] https://open.kattis.com/problems/keyboardconcert
 *	DP - Save off the best you can do for each keyboard note-by-note
 */
"""

from math import inf

def main():
	# Input
	n,m = [int(i) for i in input().split()]
	instruments = list()
	for i in range(n):
		instruments.append(set([int(j) for j in input().split()[1:]]))
	notes = [int(i) for i in input().split()]

	# min switches needed for the note (row) on this board (col)
	memo = [[inf for j in range(n)] for i in range(m)]
	# Save off the minimum to speed things up
	mins = [1]

	for i in range(n):
		if notes[0] in instruments[i]:
			memo[0][i] = 0

	for i in range(1, m):
		for j in range(n):
			# Try not to switch instruments (if possible)
			if notes[i] in instruments[j] and notes[i-1] in instruments[j]:
				memo[i][j] = memo[i-1][j]
			# See if switching anyway is better than not switching
			memo[i][j] = min(memo[i][j], mins[-1]+1)
		mins.append(min(memo[i]))
	print(min(memo[-1]))


	for i in range(len(memo)):
		print(memo[i], notes[i])

if __name__ == "__main__":
	main()