"""
/*	Turner Atwood
 *	10/16/18
 *	Maximum Rent [3.1] (https://open.kattis.com/problems/maximumrent)
 *	Python 3 was too slow, but Python2 is fine
 */
"""

from math import ceil

def main():
	a, b = [int(i) for i in raw_input().split(" ")]
	m, s = [int(i) for i in raw_input().split(" ")]
	max_rent = 0
	# Calculate elements along line rather than finding the intersection
	for y in range(1,m):
		x = m-y
		if 2*x < (s-y):
			break
		max_rent = max(max_rent, a*x+b*y)
	print max_rent

if __name__ == "__main__":
	main()