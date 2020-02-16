"""
/*	Turner Atwood
 *	1/29/20
 *	A Favourable Ending [4.6] https://open.kattis.com/problems/favourable
 *	Topological Sort to find a correct order to asses path counts
 */
"""

from copy import deepcopy
from queue import deque

def main():
	z = int(input())
	for _ in range(z):
		
		# Data structures needed
		children = dict()
		parents = dict()
		paths_to = dict()
		favourable_leaves = set()

		# Input

		s = int(input())
		for i in range(s):
			section = input().split()
			index = int(section[0])
			paths_to[index] = 0
			# Branch
			if len(section) == 4:
				children[index] = set()
				for child in section[1:]:
					child = int(child)
					if child not in parents:
						parents[child] = set()
					parents[child].add(index)
					children[index].add(child)
			# Leaf
			else:
				if section[1] == "favourably":
					favourable_leaves.add(index)

		# Topological sort
		no_parents = deque([1])
		paths_to[1] = 1

		while no_parents:
			current = no_parents.popleft()
			# Branch
			if current in children:
				for child in children[current]:
					parents[child].remove(current)
					if not parents[child]:
						no_parents.append(child)
					paths_to[child] += paths_to[current]

		# Final count
		count = 0
		for leaf in favourable_leaves:
			count += paths_to[leaf]

		print(count)



if __name__ == "__main__":
	main()