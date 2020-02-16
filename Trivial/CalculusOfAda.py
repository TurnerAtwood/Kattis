"""
/*	Turner Atwood
 *	12/15/19
 *	The Calculus of Ada [2.8] https://open.kattis.com/problems/ada
 *	Trivial - List manipulation
 */
"""

def same(a):
	return len(set(a)) == 1


def main():
	vals = [int(i) for i in input().split()][1:]
	n = len(vals)

	diffs = [[i for i in vals]]
	while not same(diffs[-1]):
		new_diffs = list()
		for i in range(len(diffs[-1])-1):
			new_diffs.append(diffs[-1][i+1]-diffs[-1][i])
		diffs.append(new_diffs)
	d = n - len(diffs[-1])

	# Find the value
	diffs = diffs[::-1]
	diffs[0].append(diffs[0][0])
	for i in range(1,len(diffs)):
		diffs[i].append((diffs[i][-1] + diffs[i-1][-1]))

	print(d, diffs[-1][-1])


if __name__ == "__main__":
	main()