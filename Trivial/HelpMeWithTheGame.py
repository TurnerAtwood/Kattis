"""
/*	Turner Atwood
 *	12/14/19
 *	Help Me With The Game [2.4] https://open.kattis.com/problems/helpme
 *	Trivial - Sorting and string manipulation
 */
"""

# Constants to make life easier
piece_index = {'K': 0, 'Q': 1, 'R': 2, 'B': 3, 'N': 4, 'P': 5}
index_piece = ['K','Q','R','B','N','']
a = ord('a')

def main():
	white = [list() for i in range(6)]
	black = [list() for i in range(6)]

	for i in range(8):
		input()	# Garbage
		line = input()
		for j in range(8):
			piece = line[2 + 4*j]
			if piece == ":" or piece == ".":
				continue

			position = (8-i,chr(a+j))
			index = piece_index[piece.upper()]
			# White are uppercase
			if piece == piece.upper():
				white[index].append( (8-i,chr(a+j)) )
			else:
				black[index].append( (i,chr(a+j)) )

	# Sorting
	for i in range(6):
		white[i].sort()
		black[i].sort()
		for j in range(len(black[i])):
			black[i][j] = (8 - black[i][j][0], black[i][j][1])

	for i in range(6):
		for j in range(len(white[i])):
			white[i][j] = (index_piece[i], white[i][j][1], white[i][j][0])
		for j in range(len(black[i])):
			black[i][j] = (index_piece[i], black[i][j][1], black[i][j][0])
	
	# Smash both lists into strings (oh my god)
	white = ",".join([",".join(["".join([str(k) for k in tup]) for tup in i]) for i in white if i])
	black = ",".join([",".join(["".join([str(k) for k in tup]) for tup in i]) for i in black if i])

	# Print
	print("White:", white)
	print("Black:", black)

if __name__ == "__main__":
	main()