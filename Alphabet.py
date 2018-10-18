"""
/*	Turner Atwood
 *	10/15/18
 *	Alphabet [2.8] (https://open.kattis.com/problems/alphabet)
 *	Longest Increasing Subsequence [DP]
 */
"""

def main():
	letters = [i for i in input()]
	LIS = [1]
	overall_longest = 1

	# Classic LIS problem
	for i in range(1,len(letters)):
		current =  letters[i]
		longest = 1
		for j in range(0, i):
			if ord(letters[j]) < ord(current):
				longest = max(longest, LIS[j]+1)
		LIS.append(longest)
		overall_longest = max(overall_longest, longest)
		
	print(26-overall_longest)

if __name__ == "__main__":
	main()	