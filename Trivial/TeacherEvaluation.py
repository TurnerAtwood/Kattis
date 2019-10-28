"""
/*	Turner Atwood
 *	10/26/19
 *	Teacher Evaluation [3.1] https://open.kattis.com/problems/teacherevaluation
 *	Ad-hoc : Trivial
 */
"""

def main():
	N,P = [int(i) for i in input().split()]
	tot = sum([int(i) for i in input().split()])

	# Check impossibility
	if (P == 0 and tot != 0) or (P == 100 and tot != 100):
		print("impossible")
		return

	i = 0
	while True:
		needed = P*(N+i)-tot
		if needed >= 0 and needed <= i*100:
			print(i)
			break
		i += 1

if __name__ == "__main__":
	main()