"""
/*	Turner Atwood
 *	10/6/19
 *	Pea Soup and Pancakes [2.1] https://open.kattis.com/problems/peasoup
 *	Ad-hoc : Trival Set usage
 */
"""

def main():
	N = int(input())
	good = []

	for x in range(N):
		K = int(input())
		name = input()
		menu = [input() for i in range(K)]
		if "pea soup" in menu and "pancakes" in menu:
			good.append(name)
	if good:
		print(good[0])
	else:
		print("Anywhere is fine I guess")



if __name__ == "__main__":
	main()