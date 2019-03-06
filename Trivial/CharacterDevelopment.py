"""
/*	Turner Atwood
 *	10/15/18
 *	Character Development [2.4] (https://open.kattis.com/problems/character)
 *	Obviously Simple
 */
"""

# Find all relationships of size 1-n between n people
def main():
	num = int(input())
	print(2**num-num-1)

if __name__ == "__main__":
	main()