"""
/*	Turner Atwood
 *	10/29/18
 *	Average Speed [3.5] (https://open.kattis.com/problems/averagespeed)
 *	Ad-Hoc
 */
"""

# String time (hh:mm:ss) to floating point (hours)
def time_to_hours(time_str):
	total = 0
	total += int(time_str[0:2])
	total += int(time_str[3:5])/60
	total += int(time_str[6:8])/(60**2)
	return total

def main():
	old_distance = 0
	old_time = 0
	current_speed = 0
	while True:
		# Get a line of input at a time
		try:
			line = input().split()
		except:
			break

		# Calculate the new distance at the current time
		new_time = time_to_hours(line[0])
		time_diff = new_time - old_time
		new_distance = old_distance + current_speed*time_diff

		# QUERY
		if (len(line) == 1):
			print(line[0], "%.2f" % new_distance, "km")
		# SPEED CHANGE
		else:
			old_distance = new_distance
			current_speed = int(line[1])
			old_time = new_time


if __name__ == "__main__":
	main()