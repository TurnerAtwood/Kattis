"""
/*	Turner Atwood
 *	10/24/19
 *	Slikar [3.4] https://open.kattis.com/problems/slikar
 *	BFS Twice - For the flood then the walk
 */
"""

from collections import deque
from math import inf

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

def main():
	R,C = [int(i) for i in input().split()]
	q = deque()
	flood_times = [[inf for j in range(C)] for i in range(R)]
	walk_times =  [[inf for j in range(C)] for i in range(R)]

	start = (-1,-1)
	grid = [list(input()) for i in range(R)]
	
	# Find all start points for the flood as well as S
	for i in range(R):
		for j in range(C):
			if grid[i][j] == "*":
				q.append((i,j,0))
				flood_times[i][j] = 0
			if grid[i][j] == "S":
				start = (i,j)
				walk_times[i][j] = "."

	# BFS to determine the time at which (i,j) is flooded
	while(q):
		i,j,cost = q.popleft()
		for x,y in DIRS:
			if not (i+x >= 0 and i+x < R and j+y >= 0 and j+y < C):
				continue
			neigh = grid[i+x][j+y]
			if neigh == '.':
				# Not Visited
				if flood_times[i+x][j+y] == inf:
					flood_times[i+x][j+y] = cost + 1
					q.append((i+x,j+y,cost+1))

	result = inf
	q.append((start[0],start[1],0))
	walk_times[start[0]][start[1]] = 0

	# BFS to try to get from start to D
	while(q):
		i,j,cost = q.popleft()

		if grid[i][j] == "D":
			result = cost
			break

		for x,y in DIRS:
			if not (i+x >= 0 and i+x < R and j+y >= 0 and j+y < C):
				continue
			neigh = grid[i+x][j+y]
			if neigh == '.' or neigh == "D":
				# Not Visited and not flooded
				if walk_times[i+x][j+y] == inf and cost+1 < flood_times[i+x][j+y]:
					walk_times[i+x][j+y] = cost + 1
					q.append((i+x,j+y,cost+1))

	# Output
	if result != inf:
		print(result)
	else:
		print("KAKTUS")

if __name__ == "__main__":
	main()