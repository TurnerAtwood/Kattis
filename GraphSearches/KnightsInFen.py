"""
/*	Turner Atwood
 *	11/9/19
 *	Knights in Fen [3.1] https://open.kattis.com/problems/knightsfen
 *	BFS Backwards from the solved state
 */
"""
from collections import deque

MOVES = ((-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2))
def neighbors(index):
	result = set()
	i = index//5
	j = index%5
	for di,dj in MOVES:
		a = i + di
		b = j + dj
		if (a >=0 and a < 5 and b >= 0 and b < 5):
			result.add(5*a+b)
	return result

def gen_distances():
	# BFS
	distances = dict()
	q = deque()
	q.append((TARGET,12,0))
	distances[TARGET] = 0

	while(q):
		board,spot,dist = q.popleft()
		if dist > 9:
			break
		for neigh in neighbors(spot):
			new_board = list(board)
			new_board[spot] = board[neigh]
			new_board[neigh] = 5;
			new_board = tuple(new_board)
			if new_board not in distances:
				distances[new_board] = dist + 1
				q.append((new_board,neigh,dist+1))
	return distances

TARGET = (1,1,1,1,1,0,1,1,1,1,0,0,5,1,1,0,0,0,0,1,0,0,0,0,0)
def main():

	distances = gen_distances()

	#print(distances)
	N = int(input())
	for z in range(N):
		board = []
		for i in range(5):
			board += [ord(i) - ord('0') for i in input()]
		spot = board.index(-16)
		board[spot] = 5
		board = tuple(board)

		if board in distances:
			print(f"Solvable in {distances[board]} move(s).")
		else:
			print("Unsolvable in less than 11 move(s).")

if __name__ == "__main__":
	main()