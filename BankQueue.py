"""
/*	Turner Atwood
 *	10/13/18
 *	Bank Queue [3.8] (https://open.kattis.com/problems/bank)
 */
"""

def merge(left, right):
	result = []
	i = 0
	left_len = len(left)
	j = 0
	right_len = len(right)
	while i < left_len and j  < right_len:
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
	people = {}
	
	for i in range(num_people):
		peep_worth, peep_time = [int(i) for i in input().split(" ")]
		if not peep_time in people:
			people[peep_time] = []
		people[peep_time] += [peep_worth]

	start = max(people)
	possible = []
	total = 0
	for i in range(start,-1,-1):
		if i in people:
			possible = merge(possible, sorted(people[i]))
		try:
			total += possible.pop()
		except:
			pass
	print(total)

if __name__ == "__main__":
	main()