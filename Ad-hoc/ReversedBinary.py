"""
/*	Turner Atwood
 *	10/20/19
 *	Reversed Binary Numbers [1.4] https://open.kattis.com/problems/reversebinary
 *	Ad-hoc
 */
"""

def main():
	a = int(input())
	a = bin(a)
	a = a[::-1]
	a = a[0:-2]
	a = int(a,2)
	print(a)

if __name__ == "__main__":
	main()