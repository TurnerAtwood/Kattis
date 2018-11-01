"""
/*	Turner Atwood
 *	11/1/18
 *	Trapezoid Walkway [3.3] (https://open.kattis.com/problems/walkway)
 *	Dijkstra's Algorithm (Single-source shortest path)
 */
"""
# Used for priorityqueue in Python
import heapq as hq

# Stores all relevant information for a paving stone
class Node:
	def __init__(self,a,b,h):
		# a,b are the 2 sides
		self.a = a
		self.b = b
		# Used stores which side is no longer available
		self.used = 0
		self.cost = (self.a+self.b)*h/100
		# Score is the lowest cost to get to this stone
		self.score = 0
		self.visited = False

# The trick is realizing that each stone is used maximally once
def main():
	while True:
		N = int(input())
		if N == 0:
			break
		edges = {}
		nodes = [None]
		for i in range(1,N+1):
			a,b,h = [int(i) for i in input().split()]
			stone = Node(a,b,h)
			nodes.append(stone)

			if not a in edges:
				edges[a] = set()
			if not b in edges:
				edges[b] = set()
			edges[a].add(i)
			edges[b].add(i)

		# Set up the last and first nodes --> (N+2 total nodes)
		last,first = [int(i) for i in input().split()]
		nodes[0] = Node(first,0,0)
		nodes.append(Node(last,0,0))
		edges[first].add(0)
		edges[last].add(N+1)

		# Dijkstra
		queue = [(0,0)]
		while queue:
			cScore,cVal = hq.heappop(queue)
			cNode = nodes[cVal]
			if cNode.visited:
				continue
			cNode.score = cScore
			cNode.visited = True

			if cVal == N+1:
				break

			avail = cNode.a
			if cNode.used == avail:
				avail = cNode.b

			for otherVal in edges[avail]:
				otherNode = nodes[otherVal]
				if otherNode.visited:
					continue
				otherNode.used = avail
				newScore = cScore + otherNode.cost
				hq.heappush(queue,(newScore,otherVal))
		print("%.2f"%nodes[-1].score)




if __name__ == "__main__":
	main()