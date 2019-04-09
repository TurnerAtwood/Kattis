"""
/*	Turner Atwoo
 *	4/8/19
 *	Immortal Porpoises [2.9] : (https://open.kattis.com/problems/porpoises)
 *	Computing Fibonacci numbers in O(log(N))
 *	Use DP to quickly generate F(N) based on N's binary representation
 */
"""

from math import log,ceil

bil = 10**9
period = 15 * bil/10

# Matrix multiplication for fibonacci matrices
def mult(a,b):
	res = [0,0,0,0]
	res[0] = (a[0] * b[0] + a[1] * b[2])%bil
	res[1] = (a[0] * b[1] + a[1] * b[3])%bil
	res[2] = res[1]
	res[3] = (a[2] * b[1] + a[3] * b[3])%bil
	return res

def main():
	# Make memo array
	memo = []
	power = 1
	a = [1,1,1,0]
	while (power < period):
		memo.append(a)
		a = mult(a,a)
		power *= 2

	# Get input and calculate their fib numbers
	n = int(input())
	for i in range(n):
		# The last 9 digits repeat every 1.5*10^9 numbers
		b = int(int(input().split()[1])%period)
		res = [1,0,0,1]
		digits = bin(b)
		power = 0
		# Start at 2**0 and go up from there (backwards)
		# Also get rid of the '0b' at the start of the string
		for digit in digits[2:][::-1]:
			if (digit == "1"):
				res = mult(res, memo[power])
			power += 1
		# Output
		print(i+1, res[1])

if __name__ == "__main__":
	main()