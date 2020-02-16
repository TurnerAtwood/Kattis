"""
/*	Turner Atwood
 *	12/17/19
 *	Closest Sums [3.1] https://open.kattis.com/problems/closestsums
 *	Sort the numbers and linear scan from both ends
 */
"""

from math import inf

def main():
	count = 1
	while (True):
		try:
			n = int(input())
		except:
			break

		nums = sorted([int(input()) for i in range(n)])
		m = int(input())

		# Queries:
		out = [f"Case {count}:"]

		for i in range(m):
			q = int(input())

			best = inf
			best_diff = inf
			a = 0
			b = n-1
			while (a < b):
				new_sum = nums[a] + nums[b]
				new_diff = abs(new_sum - q)
				if new_diff < best_diff:
					best = new_sum
					best_diff = new_diff

				if new_sum == q:
					break
				elif new_sum < q:
					a += 1
				else:
					b -= 1

			out.append(f"Closest sum to {q} is {best}.")

		print("\n".join(out))



		count += 1



if __name__ == "__main__":
	main()