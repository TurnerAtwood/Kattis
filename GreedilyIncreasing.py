"""
/*	Turner Atwood
 *	10/15/18
 *	Greedily Increasing Subsequence [1.9] (https://open.kattis.com/problems/greedilyincreasing)
 *	Single Linear Scan
 */
"""

def main():
	num = int(input())
	nums =[int(i) for i in input().split(" ")]
	seq = [nums[0]]
	# Check if each number can be included
	# 	If it can be, add it
	for i in range(1, len(nums)):
		look = nums[i]
		if look > seq[-1]:
			seq.append(look)

	print(len(seq))
	print(" ".join([str(i) for i in seq]))

if __name__ == "__main__":
	main()