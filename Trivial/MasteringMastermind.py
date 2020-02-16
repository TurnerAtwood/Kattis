"""
/*	Turner Atwood
 *	2/16/20
 *	Mastering Mastermind [2.5] https://open.kattis.com/problems/mastermind
 *	Ad-hoc : Trivial
 */
"""
def main():
	n,code,guess = input().split()
	n = int(n)
	r = 0
	s = 0
	unused_code = list()
	unused_guess = list()
	for i in range(n):
		c = code[i]
		g = guess[i]
		if c == g:
			r += 1
		else:
			unused_code.append(c)
			unused_guess.append(g)
	for let in set(unused_code):
		s += min(unused_code.count(let), unused_guess.count(let))

	print(r,s)


if __name__ == "__main__":
	main()