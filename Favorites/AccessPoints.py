"""
/*	Turner Atwood
 *	2/19/19
 *	Access Points [5.6]: (https://open.kattis.com/problems/accesspoints)
 *	Points are grouped together along lines to minimize
 *		the distances of points along the two axes.
 */
"""

def main():
	# Get the input points
	N = int(input())
	x_coords = []
	y_coords = []
	for i in range(N):
		line = input().split(" ")
		x_coords.append(int(line[0]))
		y_coords.append(int(line[1]))

	# The rest is partitioned into individual functions
	# X-Y coordinates can be treated individually
	x_ranges = coords_to_ranges(x_coords,N)
	y_ranges = coords_to_ranges(y_coords,N)
	original_points = list(zip(x_coords,y_coords))
	final_points = ranges_to_points(x_ranges,y_ranges,N)
	cost = points_to_cost(final_points,original_points,N)
	print(cost)

# Points are grouped by non-overlapping points
## that are pulled together
def coords_to_ranges(coords, N):
	ranges = [(coords[0],1)]
	for i in range(1,N):
		ranges.append((coords[i],1))
		# If the last range is pulled to the left of 
		## the one before it, merge them
		for ind in range(len(ranges)-1, 0, -1):
			r1 = ranges[ind]
			r2 = ranges[ind-1]
			# If the last range is to the right of the range before it
			if not r1[0] <= r2[0]:
				break

			# Replace the final two ranges with the merged one
			ranges.pop()
			ranges.pop()
			new_size = r1[1] + r2[1]
			new_avg = r1[0]*r1[1] + r2[0]*r2[1]
			new_avg /= new_size
			ranges.append((new_avg, new_size))
	return ranges

# Expand the ranges baack into points
def ranges_to_points(x_ranges,y_ranges,N):
	x_final = []
	y_final = []
	for cur_range in x_ranges:
		x_final += [cur_range[0]]*cur_range[1]
	for cur_range in y_ranges:
		y_final += [cur_range[0]]*cur_range[1]
	
	return list(zip(x_final,y_final))

# The cost of a point is its distance squared
def points_to_cost(a,b,N):
	dist = 0
	for i in range(N):
		x1,y1 = a[i]
		x2,y2 = b[i]
		new_cost = (x1-x2)**2 + (y1-y2)**2
		
		dist += new_cost
	return dist

if __name__ == "__main__":
	main()
