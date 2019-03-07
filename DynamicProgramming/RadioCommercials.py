"""
/*	Turner Atwood
 *	9/8/18
 *	Radio Commercials [2.1]: (https://open.kattis.com/problems/commercials)
 *	MAXIMUM SUBARRAY (DP)
 */	
"""

def main():
	# Get input and calculate profits
	line = input().split(" ")
	breaks = (int)(line[0])
	price = (int)(line[1])
	profits = [(int)(hour) - price for hour in input().split(" ")]
	
	# Compute the maximum subarray (Kadane's algorithm)
	max_ending_here = max_so_far = 0
	for profit in profits:
		max_ending_here = max(profit, max_ending_here + profit)
		max_so_far = max(max_so_far, max_ending_here)
	
	print(max_so_far)

if __name__ == "__main__":
	main()