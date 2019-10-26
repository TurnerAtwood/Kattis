"""
/*  Turner Atwood
 *  9/17/19
 *  Rock Climbing [4.1] https://open.kattis.com/problems/rockclimbing
 *  BFS from the top with negative cycles as exits
 */
"""
from math import inf

moves = [(-1,0), (0,-1), (0,1), (1,0)]
def get_neighbors(row, col, r, c):
    neighs = []
    for move in moves:
        spot = (row-move[0], col-move[1])
        if (spot[0] >= 0 and spot[1] >= 0 and spot[0] < r and spot[1] < c):
            neighs.append(spot)
    return neighs


def main():
    # Input
    r,c = [int(i) for i in input().split(" ")]
    input()
    rocks = [[0]*c]
    for i in range(r):
        line = input().strip().split()
        line = [int(j) for j in line]
        rocks.append(line)
    input()
    rocks.append([0]*c)

    # BFS
    costs = [[0]*c] + [[inf]*c for i in range(r)] + [[0]*c]

    # Make sure no negatives on first row
    for i in rocks[r]:
    	if i < 0:
    		print(0)
    		return

    changed = True
    while changed:
        changed = False
        for i in range(r+2):
            for j in range(c):
                old_cost = costs[i][j]
                for nh in get_neighbors(i,j,r+1,c):
                    low = min(costs[i][j], costs[nh[0]][nh[1]] + rocks[i][j])
                    costs[i][j] = max(0, low)
                if old_cost != costs[i][j]:
                    changed = True
    print(min(costs[r]))

if __name__ == "__main__":
    main()