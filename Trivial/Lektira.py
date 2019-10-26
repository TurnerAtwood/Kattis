"""
/*	Turner Atwood
 *	10/16/19
 *	Lektira [3.5] https://open.kattis.com/problems/lektira
 *	Ad-hoc
 */
"""

# a/b are indices of breakpoints
def check(word, a, b):
	return (word[0:a][::-1] + word[a:b][::-1] + word[b:][::-1])

def main():
	word = input()
	best = word
	N = len(word)
	for i in range(1,N-1):
		for j in range(i+1,N):
			attempt = "".join(check(word,i,j))
			if attempt < best:
				best = attempt

	print(best)

if __name__ == "__main__":
	main()