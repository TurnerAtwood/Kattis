"""
/*	Turner Atwood
 *	10/13/18
 *	Bank Queue [3.5] (https://open.kattis.com/problems/bank)
 *	Start at the last minute someone will leave, and take care of 
 ** the biggest element each minute going backwards
 **	This way, the least is lost at each possible minute
 */
"""

# Merge step from merge sort
## Merges two sorted lists into one sorted list
def merge(left, right):
	result = []
	i = 0
	left_len = len(left)
	j = 0
	right_len = len(right)
	while i < left_len and j < right_len:
		left_val = left[i]
		right_val = right[j]
		if right_val > left_val:
			result.append(left_val)
			i += 1
		else:
			result.append(right_val)
			j += 1

	if i == left_len:
		result += right[j:]
	if j == right_len:
		result += left[i:]

	return result

def main():
	num_people, close_time = [int(i) for i in input().split(" ")]
	# Map: Departure Time -> List of people 
	people = {}
	
	# Place people into buckets based on when they will leave
	for i in range(num_people):
		peep_worth, peep_time = [int(i) for i in input().split(" ")]
		if not peep_time in people:
			people[peep_time] = []
		people[peep_time] += [peep_worth]

	# Start at the latest time possible	
	start = max(people)
	possible = []
	total = 0
	# Go backwards from latest time -> present (time = 0)
	for i in range(start,-1,-1):
		# If more people can be served at this time, consider them
		if i in people:
			possible = merge(possible, sorted(people[i]))
		# possible is sorted list, so just get the largest element every minute
		try:
			total += possible.pop()
		# No people to serve at minute i
		except:
			pass
	# Output
	print(total)

if __name__ == "__main__":
	main()
