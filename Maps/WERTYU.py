"""
/*	Turner Atwood
 *	4/9/19
 *	WERTYU [3.0] : (https://open.kattis.com/problems/wertyu)
 *	TRIVIAL - Construct a map and use it for every character
 */
"""

def main():
	# Build the translation map
	## Char at i points to char at i-1
	line = "  `1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./"
	shift = dict()
	for i in range(1, len(line)):
		shift[line[i]] = line[i-1]
	inpLine = []
	# Do the same thing for all of the lines of input
	try:
		while(True):
			outLine = []
			# Translate every char in the input
			for char in input():
				outLine.append(shift[char])
			print("".join(outLine))
	except:
		pass
	


if __name__ == "__main__":
	main()