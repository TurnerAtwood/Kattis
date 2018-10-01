"""
/*	Turner Atwood
 *	9/22/18
 *	Compound Words [1.6]: (https://open.kattis.com/problems/compoundwords)
 */	
"""

def main():
	result = set()
	words = []
	# Get all the lines of input
	while(True):
		try:
			words += input().split(" ")
		except:
			break
	word_num = len(words)
	for i in range(0, word_num):
		word_a = words[i]
		for j in range(i+1, word_num):
			word_b = words[j]
			result.add(word_a + word_b)
			result.add(word_b + word_a)
	print("\n".join(sorted(result)))

if __name__ == "__main__":
	main()