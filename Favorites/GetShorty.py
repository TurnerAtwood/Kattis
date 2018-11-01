"""
/*	Turner Atwood
 *	11/1/18
 *	Get SHorty [3.8] (https://open.kattis.com/problems/getshorty)
 *	Dijkstra's Algorithm (Single-source shortest path)
 */
"""

# Used a heap as a priorityQueue
import heapq as hq

# Node used to store vertex information in one place
class Node:

	def __init__(self, i):
		self.edges = {}
		self.value = i
		self.visited = False;
		self.score = 0;

	# Replace exisiting edges with better ones
	def add(self,target, weight):
		if not target in self.edges:
			self.edges[target] = weight
		elif self.edges[target] < weight:
			self.edges[target] = weight

def main():
	while True:
		N,M = [int(i) for i in input().split()]
		if N == 0 and M == 0:
			break

		# Corridor input (Build weighted edge list in Nodes)
		nodes = [Node(i) for i in range(N)]
		for _ in range(M):
			line = input().split()
			a = int(line[0])
			b = int(line[1])
			w = float(line[2])
			nodes[a].add(b,w)
			nodes[b].add(a,w)

		# Dijsktra's
		queue = [(-1,0)]
		while queue:
			# Big mess to get all the info needed
			#	Couldn't keep nodes in the queue
			cScore, cVal = hq.heappop(queue)
			cNode = nodes[cVal]
			cScore *= -1
			if cNode.visited:
				continue

			cNode.score = cScore
			cNode.visited = True

			# Early exit condition
			if cNode.value == N-1:
				break

			# Update unvisited edges from the current vertex
			#	Better paths will just appear before worse
			#	ones in the priority queue, the latter are ignored
			for neigh in cNode.edges:
				otherNode = nodes[neigh]
				if otherNode.visited:
					continue
				possScore = cScore*cNode.edges[neigh]
				hq.heappush(queue,(-1*possScore, otherNode.value))

		# Output (Path guaranteed to exist)
		res = nodes[-1].score
		print("%1.4f"%res)

if __name__ == "__main__":
	main()