"""
/*	Turner Atwood
 *	12/14/19
 *	Euler's Number [1.8] https://open.kattis.com/problems/eulersnumber
 *	Trivial - math
 */
"""

def main():
	denom = 1
	num = min(160, int(input()))
	total = 1.0

	for i in range(1, num+1):
		denom *= i
		total += 1.0/denom

	return total

if __name__ == "__main__":
	print(main())