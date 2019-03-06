"""
/*	Turner Atwood
 *	3/5/19
 *	Okviri [1.8] : (https://open.kattis.com/problems/okviri)
 *	Pattern matching
 */
"""

def main():
	# Choose which columns surround a letter based on where it is in the string
	## Lots of nuanced edge cases
	line = input();
	size = 1 + 4*len(line)
	uno = list('..#..')
	dos = list('.#.#.')
	tre = list('#.#.#')
	uno_s = list('..*..')
	dos_s = list('.*.*.')
	tre_s = list('*.*.*')
	cols = [i for i in uno] #always how it starts
	for i in range(len(line)):
		tre[2] = line[i]
		tre_s[2] = line[i]
		# Assume the first col here is from the start or a * col
		if (i%3 == 0):
			cols += dos
			cols  += tre
			cols += dos
			cols += uno
		# Never try to add the last row, it could  be replaced with a * col
		elif (i%3 == 1):
			cols += dos
			cols += tre
			cols += dos
		# Print full * pattern - it takes priority
		else:
			cols += uno_s
			cols += dos_s
			cols += tre_s
			cols += dos_s
			cols += uno_s
	# Correct size if needed
	if (len(line)%3 == 2):
		cols += uno
	# Turn from columns into rows and print
	for i in range(5):
		row = []
		for j in range(i,len(cols),5):
			row += cols[j]
		print(''.join(row))

if __name__ == "__main__":
	main()