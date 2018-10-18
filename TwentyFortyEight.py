"""
/*	Turner Atwood
 *	9/8/18
 *	2048 [2.4]: (https://open.kattis.com/problems/2048)
 */	
"""

def _set_val(spot, val, board):
	x,y = spot[0], spot[1]
	if x in [0,1,2,3] and y in [0,1,2,3]:
		board[x][y] = val
		return board
	return -1

# Return board[x][y] if in range, -1 otherwise
def _get_val(spot, board):
	x,y = spot[0], spot[1]
	if x in [0,1,2,3] and y in [0,1,2,3]:
		return board[x][y]
	return -1

# Sets up the move stack based on direction
def _make_movement(move):
	if move == 0:
		mvmt = [(i,1) for i in range(4)]
	if move == 1:
		mvmt = [(1,i) for i in range(4)]
	if move == 2:
		mvmt = [(i,3) for i in range(4)]
	if move == 3:
		mvmt = [(3,i) for i in range(4)]
	return list(reversed(mvmt))

def main():
	# Build the board
	board = [[0 for i in range(4)] for j in range(4)]
	already_combined = []
	for i in range(4):
		board[i] = [(int)(num) for num in input().split(" ")]
	# Set up direction and moves stack
	move = (int)(input())
	directions = {0: (-1,0), 1: (0,-1), 2: (1,0), 3: (0,1)} # (x,y) - kinda confusing
	mv_dr = directions[move]
	moves = _make_movement(move)
	
	# Go through moves on the stack, moving items in given direction if possible
	while moves:
		current_spot = moves.pop()
		next_spot = (current_spot[0]+mv_dr[1], current_spot[1]+mv_dr[0]) 
		current_val =  _get_val(current_spot, board)
		next_val    =  _get_val(next_spot, board)
		if current_val != -1:
			# Add in a spot backwards if not over the edge
			back_spot = (current_spot[0]-mv_dr[1],current_spot[1]-mv_dr[0])
			moves.append(back_spot)

			if next_val == 0 and current_val != 0:
				board[next_spot[0]][next_spot[1]] = current_val
				board = _set_val(next_spot, current_val, board)
				board = _set_val(current_spot, 0, board)
				moves.append(next_spot)
				
			# NEED TO CHECK CHANGED MATRIX
			elif next_val == current_val and next_spot not in already_combined:
				board = _set_val(current_spot, 0, board)
				board = _set_val(next_spot, next_val*2, board)
				already_combined += [next_spot]
			
	[print(" ".join([str(i) for i in line])) for line in board]

if __name__ == "__main__":
	main()