"""
/*	Turner Atwood
 *	4/2/19
 *	Image Decoding [3.1] : (https://open.kattis.com/problems/imagedecoding)
 *	Ad-hoc
 */
"""

import sys

def main():
	N = int(input())
	result = []
	# Each individual image
	while N != 0:
		image = []
		# Each line of the image
		lengths = set()
		for z in range(N):
			line = input().split()
			# Initial character
			out = line[0]
			length = 0
			# Print the indicated number while swapping characters
			for num in line[1:]:
				length += int(num)
				for i in range(int(num)):
					image += [out]
				if out == "#":
					out = "."
				else:
					out = "#"
			image += "\n"
			# Add the length of this line to the set of lengths
			lengths.add(length)

		# If more than one length - there was an error
		if (len(lengths) > 1):
			image += "Error decoding image\n"
		result += ["".join(image)]
		N = int(input())
		
	print(("\n".join(result)).strip())

if __name__ == "__main__":
	main()