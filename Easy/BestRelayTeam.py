"""
/*	Turner Atwood
 *	10/15/18
 *	Best Relay Team [2.6] (https://open.kattis.com/problems/bestrelayteam)
 */
"""

def main():
	num = int(input())
	first_times = []
	other_times = []
	# Separate input into lists of runners first and other leg times
	#	The name of the runner is stored with the time in a tuple
	for i in range(num):
		line = input().split(" ")
		name = line[0]
		first = float(line[1])
		other = float(line[2])
		first_times.append((first,name))
		other_times.append((other,name))

	# The only times that matter are the top 4 for each category
	first_times = sorted(first_times)[0:5]
	other_times = sorted(other_times)[0:5]

	best_time = 100000000
	best_squad = []
	# Try all 4 fastest first times
	for first in first_times:
		this_time = first[0]
		this_squad = [first[1]]

		# Get the best 3 other times
		for other in other_times:
			# Skip the first leg runner
			if other[1] == first[1]:
				continue
			# End once 4 runners are chosen
			if len(this_squad) == 4:
				break
			this_time += other[0]
			this_squad.append(other[1])

		# If the time is the best so far, save off the names of the runners
		if this_time < best_time:
			best_time = this_time
			best_squad = this_squad
			
	print(best_time)
	print("\n".join(best_squad))

if __name__ == "__main__":
	main()