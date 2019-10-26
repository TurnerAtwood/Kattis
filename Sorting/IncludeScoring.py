"""
/*	Turner Atwood
 *	8/27/19
 *	#Include<scoring> [3.5] https://open.kattis.com/problems/includescoring
 *	Sort the scores then evenly distribute any ties
 */
"""

from sys import stdin, stdout
from math import ceil
from pprint import pprint

def main():
	n = int(stdin.readline())

	scoreValues = [100,75,60,50,45,40,36,32,29,26,24,22,20,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
	scoreValues += [0 for _ in range(30-n)]

	contest = []
	for i in range(n):
		person = [int(j) for j in stdin.readline().split()]
		person[1] = -1 * person[1]
		person[2] = -1 * person[2]
		person.append(i)
		contest.append(tuple(person))
	contest = sorted(contest, reverse=True)
	
	scores = [0 for i in range(n)]
	tieIndex = 0
	for i in range(n):
		a = contest[i]
		if i != n-1:
			b = contest[i+1]
		else:
			# The last person will always end a "tie"
			b = [-1]
		# Not a tie between a and b
		if a[0]!=b[0] or a[1]!=b[1] or a[2]!=b[2]:
			# Handle the tie
			score = sum(scoreValues[tieIndex:i+1])
			score = ceil(score / (i+1 - tieIndex))
			for j in range(tieIndex, i+1, 1):
				index = contest[j][-1]
				scores[index] = score + contest[j][3]

			# Reset the tie
			tieIndex = i+1

	print("\n".join([str(i) for i in scores]))
	
if __name__ == "__main__":
	main()