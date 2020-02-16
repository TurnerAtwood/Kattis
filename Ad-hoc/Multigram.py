"""
/*	Turner Atwood
 *	11/4/19
 *	Multigram [2.7] https://open.kattis.com/problems/multigram 
 *	Ad-hoc : Use maps to efficiently count word frequencies
 */
"""

def letterFreq(letters):
	freqs = dict()
	for letter in letters:
		if not letter in freqs:
			freqs[letter] = 0
		freqs[letter] += 1
	return freqs

def main():
	letters = input()
	total_size = len(letters)

	# Try every size multigram
	for size in range(1,total_size//2 + 1):
		if total_size%size != 0:
			continue
		bad = False
		base_freq = letterFreq(letters[0:size])
		for i in range(size, total_size, size):
			if base_freq != letterFreq(letters[i:i+size]):
				bad = True
				break
		if not bad:
			print(letters[0:size])
			return
	print(-1)

if __name__ == "__main__":
	main()