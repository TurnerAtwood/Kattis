"""
/*	Turner Atwood
 *	10/31/19
 *	Mountain Biking [2.9] https://open.kattis.com/problems/mountainbiking
 *	Ad-hoc : Estimate the integral using a binary search
 */
"""

from math import cos,sqrt,pi

# Velocity from acceleration, time, and velocity
def f(a,t,v):
	return 0.5*a*t*t + v*t

# Binary Search for the time at a given a,d, and v_0
def findTime(d,a,v):
	t = 0
	while (f(a,t,v) < d):
		t += 10

	low = t - 10
	high = t
	while (high - low >= 0.000000001):
		if f(a,(low+high)/2,v) < d:
			low = (low+high)/2
		else:
			high = (low+high)/2
	return (low+high)/2

def main():
	# Input
	line = input().split()
	N = int(line[0])
	g = float(line[1])
	slopes = list()
	for i in range(N):
		a,b = [int(i) for i in input().split()]
		slopes.append((a,b))

	# Repeatedly calculate velocities using the binary search
	for i in range(N):
		v = 0
		for j in range(i,N):
			d = slopes[j][0]
			a = g*cos(pi*slopes[j][1]/180)
			t = findTime(d,a,v)
			v = a*t + v
		print(v)

if __name__ == "__main__":
	main()