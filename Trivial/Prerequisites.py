"""
/*	Turner Atwood
 *	2/18/19
 *	Prerequisites [2.1]: (https://open.kattis.com/problems/prerequisites)
 *	Using a set to count instances
 */
"""

def main():
	while True:
		line = input().split(" ")
		if len(line) == 1:
			break

		k = int(line[0])
		m = int(line[1])
		chosen = set(input().split(" "))
		fail = False
		for i in range(m):
			line = input().split(" ")
			needed = int(line[1])
			allow = set(line[2:])
			gotten = len(allow.intersection(chosen))
			if needed > gotten:
				fail = True
		if fail:
			print('no')
		else:
			print('yes')


if __name__ == "__main__":
	main()