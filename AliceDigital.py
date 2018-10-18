"""
/*	Turner Atwood
 *	10/16/2018
 *	Alice in the Digital World [4.3] (https://open.kattis.com/problems/alicedigital)
 */
"""

def main():
	for _ in range(int(input())):
		# Inputs: size of array, minimum element, and array of numbers
		num, min_el = [int(i) for i in input().split(" ")]
		line = input().split(" ")
		min_el_locs = [-1]
		nums = []
		# Parst the list of ints and get all elements <=min
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