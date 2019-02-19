"""
/*	Turner Atwood
 *	2/17/19
 *	Flying Safely [1.6]: (https://open.kattis.com/problems/flyingsafely)
 *	A city of size N only requires N-1 pilots
 */
"""

def main():
	Z = int(input())
	for j in range(Z):
		N,M = [int(i) for i in input().split(" ")]
		print(N-1)
		[input() for i in range(M)]


if __name__ == "__main__":
	main()