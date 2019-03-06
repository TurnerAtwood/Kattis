"""
/*	Turner Atwood
 *	2/26/19
 *	Engineering English [2.2] : (https://open.kattis.com/problems/engineeringenglish)
 *	Basic Set example
 */
"""

def main():
	# Set of all words seen
	seen = set()
	while (True):
		# Print each line when done with it
		out = []
		try:
			line = input().lower().split(" ")
		except:
			break
		# Print a . if word already seen
		for word in line:
			if word in seen:
				out += ["."]
			else:
				out += [word]
				seen.add(word)
		print(" ".join(out))

if __name__ == "__main__":
	main()