"""
/*	Turner Atwood
 *	11/20/19
 *	Sjecista [1.8] https://open.kattis.com/problems/sjecista 
 *	Ad-hoc : Basic math
 */
"""

def main():
	n = int(input())
	if n == 3:
		print(0)
		return

	# n Choose 4
	top,bot = 1,1
	for i in range(n-4):
		top *= (n-i)
		bot *= (i+1)
		
	print(top//bot)

if __name__ == "__main__":
	main()