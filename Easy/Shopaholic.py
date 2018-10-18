"""
/*	Turner Atwood
 *	10/15/18
 *	Shopaholic [2.7] (https://open.kattis.com/problems/shopaholic)
 */
"""

def main():
	num = int(input())
	# Consider the items in sorted (descending) order
	costs = sorted([int(i) for i in input().split(" ")])[::-1]
	saved = 0
	# Take groups of 3 at a time, the 3 element is free, or 'saved'
	for i in range(2, len(costs), 3):
		saved += costs[i]
	print(saved)

if __name__ == "__main__":
	main()	