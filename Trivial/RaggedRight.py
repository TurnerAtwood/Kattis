"""
/*	Turner Atwood
 *	10/20/19
 *	Ragged Right [1.9] https://open.kattis.com/problems/raggedright
 *	Ad-hoc
 */
"""

def main():
	lens = []
	try:
		while(True):
			lens.append(len(input()))
	except:
		pass

	top = max(lens)
	total = 0
	for i in lens[:-1]:
		total += (top-i)**2
	print(total)

if __name__ == "__main__":
	main()