"""
/*	Turner Atwood
 *	10/15/18
 *	Amsterdam Distance [2.7] (https://open.kattis.com/problems/amsterdamdistance)
 */
"""

from math import pi

def main():
	line = input().split(" ")
	seg_num = int(line[0])
	ring_num = int(line[1])
	radius = float(line[2])
	layout = [seg_num, ring_num, radius]

	line = input().split(" ")
	p1 = [int(i) for i in line[0:2]]
	p2 = [int(i) for i in line[2:4]]

	# Try to match the ring then move along the arc
	# STRAIGHT PART (match segment num)
	dist = abs(p1[1]-p2[1])*radius/ring_num

	# AROUND THE ARC (match the ring num)
	ring = min(p1[1], p2[1])
	ring_circ = pi*(radius*ring/ring_num)
	dist += abs(p1[0]-p2[0])*ring_circ/seg_num

	# Compare to if you had just gone straight to the origin and back out
	dist = min(dist, (p1[1]+p2[1])*radius/ring_num)

	print(dist)

if __name__ == "__main__":
	main()