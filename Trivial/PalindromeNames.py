"""
/*	Turner Atwood
 *	2/26/19
 *	Palindrome Names [3.7] : (https://open.kattis.com/contests/rw4cev/problems/names)
 *	Try adding 0,1,2,...,N (N = len(name)) and get the minimum cost
 */
"""

def main():
	name = input()
	best = 100
	N = len(name)
	for i in range(N):
		new_name = name+name[0:i][::-1]
		rev = new_name[::-1]
		diff = sum([1 for i in range(len(new_name)//2) if new_name[i] != rev[i]]) + i
		best = min(best, diff)
	print(best)
		

if __name__=="__main__":
	main()