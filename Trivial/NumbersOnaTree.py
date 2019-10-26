"""
/*	Turner Atwood
 *	10/16/19
 *	Numbers On a Tree [2.0] https://open.kattis.com/problems/numbertree
 *	Ad-hoc : Binary
 */
"""

import math

def main():
	H,path = input().split(" ")
	H = int(H) + 1

	N = len(path)+1
	total = 0
	exp = H - 1
	while (N < H):
		total += int(math.pow(2, exp))
		exp -= 1
		N += 1

	binary = "0"
	for move in path:
		if move == "L":
			binary += "1"
		else:
			binary += "0"

	total += int(binary,2)
	print(total+1)

if __name__ == "__main__":
	main()