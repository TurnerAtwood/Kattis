"""
/*	Turner Atwood
 *	11/4/19
 *	Parket [2.6] https://open.kattis.com/problems/parket 
 *	Ad-hoc : Solve a linear equation using a linear scan
 */
"""

def main():
	outer,inner = [int(i) for i in input().split()]
	area = outer + inner

	for i in range(2,area//2):
		if (area%i != 0):
			continue
		j = area//i
		if (2*i + 2*j == outer + 4):
			print(j,i)
			break

if __name__ == "__main__":
	main()