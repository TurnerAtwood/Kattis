"""
/*	Turner Atwood
 *	11/3/19
 *	Locked Treasure [3.0] https://open.kattis.com/problems/lockedtreasure
 *	Ad-hoc : Calculate a combination
 */
"""

def main():
	N = int(input())
	for z in range(N):
		a,b = [int(i) for i in input().split()]
		b -= 1
		
		# a choose b
		top,bot = 1,1
		for i in range(a-b):
			top *= (a-i)
			bot *= (i+1)
		print(top//bot)

if __name__ == "__main__":
	main()