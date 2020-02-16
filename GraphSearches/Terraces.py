"""
/*	Turner Atwood
 *	12/16/20
 *	Terraces [3.5] https://open.kattis.com/problems/terraces
 *	Union-Find : Union terraces of same levels then check runnoff
 */
"""

p = list()
sizes = list()
m,n = 0,0

def main():
	global p,sizes
	global m,n
	# MxN matrics
	n,m = [int(i) for i in input().split()]
	heights = list()
	for i in range(m):
		heights += [int(num) for num in input().split()]
	
	sizes = [1 for i in range(n*m)]
	p = [i for i in range(n*m)]

	for a in range(n*m):
		neighbors = neighs(a)
		for b in neighbors:
			if heights[a] == heights[b]:
				union(a,b)
	
	# Collapse all items to have the same parent
	for i in range(m*n):
		find(i)

	haslower = [False for i in range(m*n)]

	reps = set()
	for a in range(m*n):
		if a == p[a]:
			reps.add(a)
		for b in neighs(a):
			if heights[b] < heights[a]:
				haslower[p[a]] = True

	total = 0
	for rep in reps:
		if not haslower[rep]:
			total += sizes[rep]
	print(total)
	
def pprint(p):
	for i in range(m):
		print(p[i*n:(i+1)*n])

def neighs(a):
	neighs = []
	# Left
	if a-1 >= 0 and a//n == (a-1)//n:
		neighs.append(a-1)
	# Right
	if a+1 < m*n and a//n == (a+1)//n:
		neighs.append(a+1)
	# Up
	if a-n >= 0:
		neighs.append(a-n)
	# Down
	if a+n < m*n:
		neighs.append(a+n)
	return neighs

def union(a,b):
	global p
	p_a = find(p[a])
	p_b = find(p[b])
	if p_a < p_b:
		p[p_a] = p_b
		sizes[p_b] += sizes[p_a]
	if p_b < p_a:
		p[p_b] = p_a
		sizes[p_a] += sizes[p_b]

def find(a):
	global p
	if a == p[a]:
		return a
	p[a] = find(p[a])
	return p[a]

if __name__ == "__main__":
	main()