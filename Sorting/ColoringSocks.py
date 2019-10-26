"""
/*	Turner Atwood
 *	3/25/19
 *	Coloring Socks [2.5] https://open.kattis.com/problems/color
 *	Sort the socks then Ad-hoc
 */
"""

def main():
	S,C,K = [int(i) for i in input().split()]
	socks = [int(i) for i in input().split()]
	socks.sort()

	machines = 0
	cur_color = socks[0]
	cur_cap  = 0
	for i in range(S):
		# Check to see if the machine is full
		if cur_cap == C:
			machines += 1
			cur_cap = 0

		sock = socks[i]

		# If the machine is empty, change the color to the current sock
		if cur_cap == 0:
			cur_color = sock

		# If the new sock is close enough to the original, throw it in
		if abs(sock-cur_color) <= K:
			cur_cap += 1
		# If not, start a new machine with that color
		else:
			machines += 1
			cur_cap = 1
			cur_color = sock

	# Count another machine if the last one is unfinished
	if cur_cap > 0:
		machines += 1
	print(machines)


if __name__ == "__main__":
	main()