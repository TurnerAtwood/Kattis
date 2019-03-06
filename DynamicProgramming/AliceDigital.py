"""
/*	Turner Atwood
 *	10/16/2018
 *	Alice in the Digital World [3.9] (https://open.kattis.com/problems/alicedigital)
 *	Generatethe largest possible subarray containing each instance of min_el q as min
 **	If these got large enough, a memo array (DP) could be used to speed things up
 **	ex: q=4 [5,4,6,3,4,4,5,2,6,5,4] -> [[5,4],[4,6],[4],[4,5],[6,5,4]]
 */
"""

def main():
	for _ in range(int(input())):
		# Inputs: size of array, minimum element, and array of numbers
		num, min_el = [int(i) for i in input().split(" ")]
		line = input().split(" ")
		min_el_locs = [-1]
		nums = []
		# Parse the list of ints and get all elements <= min
		for i in range(len(line)):
			el = int(line[i])
			nums.append(el)
			if el <= min_el:
				min_el_locs.append(i)
		min_el_locs.append(num)

		# Find the largest array bounded inside 2 almost adjacent "minimum elements"
		##	that contains one instance of the minimum number
		best = 0
		for i in range(1, len(min_el_locs)-1):
			check = nums[min_el_locs[i-1]+1:min_el_locs[i+1]]
			if min_el in check:
				best = max(best, sum(check))

		print(best)

if __name__ == "__main__":
	main()