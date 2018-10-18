"""
/*	Turner Atwood
 *	10/16/18
 *	ASCII Figure Rotation [3.7] (https://open.kattis.com/problems/asciifigurerotation)
 */
"""

def main():
	first = True
	while True:
		height = int(input())
		if height == 0:
			break
		# Don't print a space on the first figure
		if not first:
			print()
		else:
			first = False

		# Read in lines and keeep track of the longest line
		art = []
		width = 0
		for i in range(height):
			line = [i for i in input()]
			art.append(line)
			width = max(width, len(line))
		
		# Pad short lines with spaces (on the end)
		for i in range(height):
			line = art[i]
			diff = width-len(line)
			line += [' ']*diff
			
		# ROTATE - Traverse the original such that we
		#			build the new left to right and top down
		rot_art = []
		# Go from left to right
		for j in range(0, width):
			# Go down to up
			new_row = []
			for i in range(height-1, -1, -1):
				look = art[i][j]
				# Switch the character in these cases
				if look == "|":
					look = '-'
				elif look == "-":
					look = '|'
				new_row.append(look)

			# Building row by row
			rot_art.append(new_row)

		# Get rid of all trailing spaces on each line
		for line in rot_art:
			while line[-1] == ' ':
				line.pop()
			# line by line as they are cleaned
			print(''.join(line))

if __name__ == "__main__":
	main()