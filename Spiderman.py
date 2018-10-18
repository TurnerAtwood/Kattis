"""
/*	Turner Atwood
 *	10/16/18
 *	Spiderman's Workout [3.9] (https://open.kattis.com/problems/spiderman)
 *	Bottom-Up [DP]?
 */
"""


def main():
	for _ in range(int(input())):
		num = int(input())
		nums = [int(i) for i in input().split(" ")]
		overall_path = []
		# HOLDS: height, path, top_height
		# Keeps the height stored with the path taken and its maxx height

		poss_path = {0:('',0)}
		for i in range(num):
			# The current height being considered
			current =  nums[i]
			new_paths = dict()

			# try to go up and down from every possible height
			for pathHeight in poss_path:
				#UP:
				# Compute new values
				new_height = pathHeight + current
				path = poss_path[pathHeight]
				new_path = path[0] + 'U'
				new_max = max(path[1], new_height)

				#ADD TO new_paths if it is an optimal path for the new_height
				if new_height not in new_paths:
					new_paths[new_height] = (new_path, new_max)
				else:
					old_max = new_paths[new_height][1]
					if new_max < old_max:
						new_paths[new_height] = (new_path, new_max)

				#DOWN:
				# Compute new values
				new_height = pathHeight - current
				# Cannot go below the floor
				if new_height < 0:
					continue
				path = poss_path[pathHeight]
				new_path = path[0] + 'D'
				new_max = max(path[1], new_height)

				#ADD TO new_paths if it is an optimal path for the new_height
				if new_height not in new_paths:
					new_paths[new_height] = (new_path, new_max)
				else:
					old_max = new_paths[new_height][1]
					if new_max < old_max:
						new_paths[new_height] = (new_path, new_max)
			
			poss_path = new_paths		

		if 0 in poss_path:
			print(''.join(poss_path[0][0]))
		else:
			print("IMPOSSIBLE")



if __name__ == "__main__":
	main()