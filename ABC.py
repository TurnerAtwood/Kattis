"""
/*	Turner Atwood
 *	9/11/18
 *	ABC [1.7]: (https://open.kattis.com/problems/abc)
 */	
"""

def main():
	nums = sorted([(int)(i) for i in input().split(" ")])
	letters = [i for i in input()]
	let = ['A', 'B', 'C']
	letter_map = {let[i]:nums[i] for i in [0,1,2]}
	print(" ".join([str(letter_map[i]) for i in letters]))

if __name__ == "__main__":
	main()