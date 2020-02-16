"""
/*	Turner Atwood
 *	12/14/19
 *	Cetiri [1.8] https://open.kattis.com/problems/cetiri
 *	Trivial - Sort and check differences
 */
"""

def main():
	numbers = sorted([int(i) for i in input().split()])

	diff = numbers[1] - numbers[0]
	diff_index = len(numbers)-1


	for i in range(len(numbers)-1):
		new_diff = numbers[i+1] - numbers[i]
		if new_diff < diff:
			return (numbers[i-1]+new_diff)

		elif new_diff > diff:
			return (numbers[i]+diff)
	
	return (numbers[-1]+diff)

if __name__ == "__main__":
	print(main())