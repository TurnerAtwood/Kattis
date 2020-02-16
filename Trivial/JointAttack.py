"""
/*	Turner Atwood
 *	2/16/20
 *	Joint Attack [2.5] https://open.kattis.com/problems/jointattack
 *	Ad-hoc : Trivial math
 */
"""

def main():
	n = int(input())
	xs = [int(i) for i in input().split()][::-1]

	top = 1
	bot = xs[0]
	for i in range(1,n):
		top = bot*xs[i] + top
		top,bot = bot,top
	print(f"{bot}/{top}")


if __name__ == "__main__":
	main()