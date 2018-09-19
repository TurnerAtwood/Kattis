"""
/*	Turner Atwood
 *	9/7/18
 *	Prinova [3.5]: (https://open.kattis.com/problems/prinova)
 */	
"""

# COMMENTS FOR THE LOVE OF GOD
def main():
	# Get boys names and sort them
	num = (int)(input())
	boys = sorted([(int)(name) for name in input().split(" ")])
	boys_dist = []
	
	# Calculate the gaps between boys (must be odd values)
	for i in range(1,num):
		score = (boys[i] - boys[i-1])//2
		if score%2 == 0:
			score -= 1
		boys_dist.append(score)

	# Add infinity to the edges to make boundary calculations easier
	boys_dist = [float("inf")] + boys_dist + [float("inf")]
	boys = [-1 * float("inf")] + boys + [float("inf")]

	# Get the required name range and make sure the edges are odd
	t_range = [(int)(name) for name in input().split(" ")]
	if t_range[0]%2 == 0:
		t_range[0] += 1
	if t_range[1]%2 == 0:
		t_range[1] -= 1

	# Find which area the boundaries are in. (Which points they fall between)
	low_area = [ind for ind,boy in enumerate(boys) if t_range[0] > boy][-1]		
	high_area = [ind-1 for ind,boy in enumerate(boys) if t_range[1] < boy][0]
	
	# Calculate the new score for the boundary areas (May or may not change boys_dist)
	boys_dist[low_area] = min(boys_dist[low_area], abs(t_range[0] - boys[low_area+1])) 
	boys_dist[high_area] = min(boys_dist[high_area], abs(t_range[1] - boys[high_area])) 
	
	# Find which area (between the boundaries) gives the highest score
	max_score, max_section = 0, 0
	for ind in range(low_area, high_area+1):
		option = boys_dist[ind]
		if option > max_score:
			max_score = option
			max_section = ind

	# Finally, calculate and print the girl's name. (Use nearby point and max_score)
	if max_section == 0:
		print(boys[1] - max_score)
	else:
		print(boys[max_section] + max_score)

if __name__ == "__main__":
	main()