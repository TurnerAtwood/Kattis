"""
/*	Turner Atwood
 *	9/12/18
 *	10 Kinds of People [5.5]: (https://open.kattis.com/problems/10kindsofpeople)
 *	UNIONFIND
 */	
"""

# Unionfind implemented over a 2D array (tuples)
class UnionFind():
	board = []

	def __init__(self, height, width):
		self.board = [[(j,i) for i in range(width)] for j in range(height)]
	
	def get(self, spot):
		return self.board[spot[0]][spot[1]]

	def set(self, spot, val):
		self.board[spot[0]][spot[1]] = val

	def find(self, spot):
		if self.get(spot) != spot:
			self.set(spot, self.find(self.get(spot)))
		return self.get(spot)

	def union(self, spot, val):
		self.set(self.find(spot), self.find(val))

	def printState(self):
		print("\n".join([str(line) for line in self.board]))


def main():
	height,width = [int(i) for i in input().split(" ")]
	board = []
	board = [[int(i) for i in input()] for line in range(height)]
	# DEBUG: Print
	print("\n".join([str(line) for line in board]))
	num_tests = int(input())
	for test_num in range(num_tests):
		points = [int(i) for i in input().split(" ")]
		start = (points[0], points[1])
		stop = (points[2], points[3])
		print(start, stop)

	# DEBUG: TESTING UNIONFIND
	a = UnionFind(10,20)
	a.printState()
	a.set((1,1), (0,1))
	a.set((2,1), (1,1))
	a.set((3,1), (2,1))
	a.set((4,1), (3,1))
	a.set((1,1), (0,1))
	a.set((2,2), (1,1))
	a.set((3,2), (2,1))
	a.set((4,2), (3,2))

	print(a.find((4,1)))
	a.printState()

if __name__ == "__main__":
	main()