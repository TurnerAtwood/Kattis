"""
/*	Turner Atwood
 *	8/28/19
 *	Divide By 100... [4.3] https://open.kattis.com/problems/divideby100
 *	Ad-hoc : A little bit of string manipulation
 */
"""

from sys import stdin

def main():
	N = [i for i in stdin.readline().strip()]
	M = len(stdin.readline().strip()) - 1
	left = []
	right = []
	if len(N) > M:
		left = N[:len(N)-M]
		right = N[len(N)-M:]
	else:
		left = ['0']
		leadZeros = ['0' for i in range(M-len(N))]
		right = leadZeros + N

	# Remove Trailing zeros
	while(right and right[-1] == '0'):
		del(right[-1])

	# Print 
	if right:
		print("".join(left + ['.'] + right))
	else:
		print("".join(left))

if __name__ == "__main__":
	main()