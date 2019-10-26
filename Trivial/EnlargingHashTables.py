"""
/*	Turner Atwood
 *	8/27/19
 *	Enlarging Hash Tables [3.6] https://open.kattis.com/problems/enlarginghashtables
 *	Ad-hoc : Testing Prime Numbers
 */
"""


def main():
	n = int(input())
	while n != 0:
		m = 2*n+1
		done = False
		while not isPrime(m):			
			m += 2

		if isPrime(n):
			print(m)
		else:
			print(f"{m} ({n} is not prime)")
		
		n = int(input())

def isPrime(n):
	upper = int(n**.5)+1
	for i in range(2,upper,1):
		if not n%i:
			return False
	return True


if __name__ == "__main__":
	main()