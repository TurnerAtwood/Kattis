"""
/*	Turner Atwood
 *	10/17/19
 *	Pipe Rotation [3.4] https://open.kattis.com/problems/piperotation
 *	Very odd BFS : Pipes are locked in place in sequence
 */
"""

move_index = [(-1,0),(0,1),(1,0),(0,-1)]
class pipe:

	def __init__(self, v):
		self.val = v
		self.open_to = {0,1,2,3}		# Up, Right, Down, Left

	# Try to remove d, return false if impossible
	def remove(self, d):
		self.open_to.discard(d)
		if self.val == 1:	# Straight
			self.open_to.discard((d+2)%4)
		return self.validate()

	# Try to remove edges based on other locked edges
	# In this case, d must be used
	def choose(self, d):
		if self.val == 1:
			# Remove the orthogonal edges
			return self.remove((d+1)%4)
		elif self.val == 2:
			# Remove the opposite edge
			return self.remove((d+2)%4)
		return True

	def validate(self):
		if self.val == 1:
			if not self.open_to:
				return False
		elif self.val == 2:
			if len(self.open_to) < 2:
				return False
			if len(self.open_to) == 2:
				if (0 in self.open_to and 2 in self.open_to) or (1 in self.open_to and 3 in self.open_to):
					return False			
		elif self.val == 3:
			if len(self.open_to) < 4:
				return False
		return True

	def is_locked(self):
		if self.val == 0:
			return False
		if self.val == 1 or self.val == 2:
			return len(self.open_to) == 2
		return True

	def __repr__(self):
		return str(self.val)


def main():
	# CONSTANTS
	offset = ord('A')

	# DIMENSIONS
	N,M = [int(i) for i in input().split()]
	
	pipes = [[pipe(0) for i in range(M+2)] for i in range(N+2)]
	
	# GRAB PIPE INPUT - INITIALIZE ALL DATA
	for i in range(1,N+1):
		line = input()
		for j in range(1,M+1):
			t = ord(line[j-1]) - offset
			pipes[i][j] = pipe(t)

	# [print(i) for i in pipes]

	locked = list()
	# LOCK ALL PIPES NEXT TO EMPTIES
	for i in range(1,N+1):
		for j in range(1,M+1):
			if pipes[i][j].val == 0:
				continue
			for k in range(4):
				m_v,m_h = move_index[k]
				neigh = pipes[i+m_v][j+m_h]
				if neigh.val == 0:
					res = pipes[i][j].remove(k)
					if not res:
						return False
			if pipes[i][j].is_locked():
				locked.append((i,j))

	visited = set()
	
	# DFS OVER ALL LOCKED PIPES TO LOCK THEIR NEIGHBORS
	while (locked):
		i,j = locked.pop()
		visited.add((i,j))
		curr = pipes[i][j]
		for k in curr.open_to:
			m_v,m_h = move_index[k]
			neigh = pipes[i+m_v][j+m_h]
			res = neigh.choose((k+2)%4)
			if not res:
				return False				

			if not (i+m_v, j+m_h) in visited and neigh.is_locked():
				locked.append((i+m_v, j+m_h)) 


	return True

def dump(pipes,N,M,op):
	out = []
	for i in range(1,N+1):
		for j in range(1,M+1):
			if op == 0:
				out.append(f"{pipes[i][j].open_to} ")
			elif op == 1:
				out.append(f"{pipes[i][j].is_locked()} ")
		out.append("\n")
	print("".join(out))

if __name__ == "__main__":
	res = main()
	if res:
		print("Possible")
	else:
		print("Impossible")