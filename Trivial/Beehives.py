"""
/*	Turner Atwood
 *	11/20/19
 *	Beehives [2.1] https://open.kattis.com/problems/beehives
 *	Ad-hoc : Check the proximity of every beehive to every other
 */
"""

def dist(h1, h2):
	return ((h1[0]-h2[0])**2 + (h1[1]-h2[1])**2)**(1/2)

def main():
	while (True):
		line = input().split()
		d = float(line[0])
		n = int(line[1])
		if d == 0.0 and n == 0:
			break

		hives = list()
		for i in range(n):
			hives.append(tuple([float(j) for j in input().split()]))
		
		sour = set()
		for i in range(n-1):
			for j in range(i+1,n):
				if dist(hives[i],hives[j]) <= d:
					sour.add(i)
					sour.add(j)
		print(f"{len(sour)} sour, {n-len(sour)} sweet")



if __name__ == "__main__":
	main()