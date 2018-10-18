"""
/*	Turner Atwood
 *	10/15/18
 *	Convex Polygon Area [2.0] (https://open.kattis.com/problems/convexpolygonarea)
 *	Simple Determinate Area Calculation
 */
"""

def main():
	for _ in range(int(input())):
		# Input
		points = [int(i) for i in input().split(" ")][1:]
		matrix = []
		for i in range(0,len(points), 2):
			matrix.append([points[i], points[i+1]])
		# Include the first point on the end
		matrix.append(matrix[0])
		
		# Calculate determinant
		total = 0
		for i in range(len(matrix)-1):
			total += matrix[i][0]*matrix[i+1][1]
			total -= matrix[i][1]*matrix[i+1][0]
			
		print(total/2)


if __name__ == "__main__":
	main()