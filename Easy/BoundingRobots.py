"""
/*	Turner Atwood
 *	10/31/188
 *	Bounding Robots [1.6] (https://open.kattis.com/problems/boundingrobots)
 */
"""

def main():
	while True:
		height,width = [int(i) for i in input().split()]
		if height == 0 and width == 0:
			break

		actual = [0,0]
		thinks = [0,0]
		dirs = {'u':[0,1], 'd':[0,-1], 'l':[-1,0], 'r':[1,0]}
		for _ in range(int(input())):
			direction, dist = input().split()
			dist = int(dist)
			move = [dist*i for i in dirs[direction]]
			thinks = [i+j for i,j in zip(thinks,move)]
			actual = [i+j for i,j in zip(actual,move)]
			# Keep the actal in bounds
			actual[0] = max(0,actual[0])
			actual[1] = max(0,actual[1])
			actual[0] = min(height-1, actual[0])
			actual[1] = min(width-1, actual[1])

		print("Robot thinks ", " ".join([str(i) for i in thinks]))
		print("Actually at ", " ".join([str(i) for i in actual]))
		print()

if __name__ == "__main__":
	main()