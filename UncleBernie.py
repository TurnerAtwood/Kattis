"""
/*	Turner Atwood
 *	9/30/18
 *	Grandpa Bernie [3.9]: (https://open.kattis.com/problems/grandpabernie)
 */	
"""
def main():
	num_trips = int(input())
	trips = {}
	for _ in range(num_trips):
		place, year = input().split(" ")
		year = int(year)
		if not place in trips:
			trips[place] = [year]
		else:
			trips[place] += [year]
	# print(trips)

	# Sort 
	for place in trips:
		trips[place] = sorted(trips[place])

	# Get queries
	num_queries= int(input())
	for _ in range(num_queries):
		location, visit_num = input().split(" ")
		visit_num = int(visit_num)
		print(trips[location][visit_num-1])

if __name__ == "__main__":
	main()