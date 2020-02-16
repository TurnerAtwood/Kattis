"""
/*	Turner Atwood
 *	11/19/19
 *	Nimionese [2.1] https://open.kattis.com/problems/nimionese
 *	Ad-hoc : Basic BFS used to find nearest letter
 */
"""

HARDS = {'b','c','d','g','k','n','p','t'}
HARDS = {ord(letter) for letter in HARDS}

# BFS
def find_nearest_hard(start):
	# Handle uppercases
	uppercase = (start.lower() != start)
	start = ord(start.lower())

	i = 0
	found = -1
	while True:
		left = start-i
		if (left in HARDS):
			found = left
			break
		right = start+i 
		if (right in HARDS):
			found = right
			break
		i += 1

	found = chr(found)
	if uppercase:
		found = found.upper()

	return found

VOWELS = {'a','o','u'}
VOWELS = {ord(let) for let in VOWELS}

# BFS
def find_nearest_soft(start):
	start= ord(start.lower())
	i = 0
	while True:
		left = start-i
		if (left in VOWELS):
			return chr(left)
		right = start+i 
		if (right in VOWELS):
			return chr(right)
		i += 1

def main():
	words = input().split()
	output = list()

	for word in words:
		syllables = [list(syl) for syl in word.split("-")]
		
		# Rule 1
		syllables[0][0] = find_nearest_hard(syllables[0][0])
		
		# Rule 2
		for syl in syllables[1:]:
			for j in range(len(syl)):
				if ord(syl[j]) in HARDS:
					syl[j] = syllables[0][0].lower()

		# Rule 3
		if ord(syllables[-1][-1].lower()) in HARDS:
			syllables[-1].append(find_nearest_soft(syllables[-1][-1]))
			syllables[-1].append("h")
		# print(syllables)

		# Formatting result
		syllables = ["".join(syl) for syl in syllables]
		syllables = "".join(syllables)
		output.append(syllables)

	print(" ".join(output))

if __name__ == "__main__":
	main()