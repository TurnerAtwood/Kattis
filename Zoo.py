"""
/*	Turner Atwood
 *	9/5/18
 *	Un-bear-able Zoo [1.6]: (https://open.kattis.com/problems/zoo)
 */	
"""

# Get each animal and put it in the map
def _map_animal_names(num):
	zoo = {}
	for i in range(num):
			animal = input().split(" ")[-1].lower()
			if animal not in zoo:
				zoo[animal] = 1
			else:
				zoo[animal] += 1
	return zoo

if __name__=="__main__":
	num = (int)(input())
	count = 1
	while (num != 0):
		zoo = _map_animal_names(num)

		# Print results and get new number
		print(f"List {count}:")
		for key in sorted(zoo):
			print(f"{key} | {zoo[key]}")
		count += 1
		num = (int)(input())