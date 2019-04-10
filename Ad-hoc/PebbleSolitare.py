"""
/*	Turner Atwood
 *	4/10/19
 *	Pebble Solitaire [2.2] : (https://open.kattis.com/problems/pebblesolitaire)
 *	Brute Force - Try every possible game and take the maximum
 */
"""

from copy import deepcopy

def main():
	# Get Input
	N = int(input())
	for i in range(N):
		board = list(input())
		# Run the search and print the result
		best = findBest(board)
		print(board.count('o') - best)

# Recursively try every move given the current board
## and return the maximum pebbles removed
def findBest(board):
	best = 0
	bestBoard = board
	# Look at every pair of adjacent spaces
	for i in range(11):
		seg = board[i:i+2]
		# Found adjacent pebbles
		if seg == ['o','o']:
			# Try to jump to the left
			if board[i-1:i+2] == list('-oo'):
				newBoard = deepcopy(board)
				newBoard[i-1] = 'o'
				newBoard[i+0] = '-'
				newBoard[i+1] = '-'
				best = max(best, 1+findBest(newBoard))
			# Try to jump to the right
			if board[i:i+3] == list('oo-'):
				newBoard = deepcopy(board)
				newBoard[i+0] = '-'
				newBoard[i+1] = '-'
				newBoard[i+2] = 'o'
				best = max(best, 1+findBest(newBoard))
	return best


if __name__ == "__main__":
	main()