"""
/*	Turner Atwood
 *	9/30/18
 *	Flexible Spaces [1.8]: (https://open.kattis.com/problems/flexible)
 *	Nested Linear Scans O(n^2)
 */	
"""

def main():
	line = input().split(" ")
	width = int(line[0])
	num = int(line[1])+2
	partitions = [0] + [int(part) for part in input().split(" ")] + [width]
	
	# Try every pair of partitions and add the size to the set
	sizes = set()
	for i in range(num):
		start = partitions[i]
		for j in  range(i+1, num):
			stop = partitions[j]
			sizes.add(stop - start)
	sizes = sorted(list(sizes))
	print(" ".join([str(i) for i in sizes]))
if __name__ == "__main__":
	main()