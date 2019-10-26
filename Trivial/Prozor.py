"""
/*	Turner Atwood
 *	10/23/19
 *	Prozor [1.6] https://open.kattis.com/problems/prozor
 *	Ad-hoc : O(N^4) :)
 */
"""

def main():
	R,S,K = [int(i) for i in input().split()]

	table = []

	for i in range(R):
		line = input()
		table.append([])
		for j in range(S):
			table[i].append(line[j])


	best = -1
	best_ind = (1,1)
	for i in range(1,R-K+2):
		for j in range(1,S-K+2):
			out = []
			flies = 0
			for x in range(K-2):
				for y in range(K-2):
					if table[i+x][j+y] == "*":
						flies += 1
					out.append(table[i+x][j+y])
				out.append("\n")
			if flies > best:
				best_ind = (i-1,j-1)
				best = flies
			# print("".join(out))

	print(best)

	a,b = best_ind
	# Replace with raquet
	for i in range(K):
		table[a+i][b] = "|"
		table[a][b+i] = "-"
		table[a+K-1][b+i] = "-"
		table[a+i][b+K-1] = "|"
	table[a][b] = "+"
	table[a+K-1][b] = "+"
	table[a][b+K-1] = "+"
	table[a+K-1][b+K-1] = "+"


	table = ["".join(i) for i in table]
	table = "\n".join(table)
	print(table)


if __name__ == "__main__":
	main()