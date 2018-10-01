"""
/*	Turner Atwood
 *	9/23/18
 *	UnDetected [3.4]: (https://open.kattis.com/problems/undetected)
 *	UNIONFIND
 */	
"""
import math

class UnionFind():
	
	def __init__(self, size):
		self.parents = [i for i in range(size)]

	def union(self, child_a, child_b):
		root_a = self.find(child_a)
		root_b = self.find(child_b)
		if root_b < root_a:
			root_a, root_b = root_b, root_a

		if not root_a == root_b:
			self.parents[root_b] = root_a

	def find(self, child):
		if self.parents[child] == child:
			return child
		self.parents[child] = self.find(self.parents[child])
		return self.parents[child]

def _touching(sensor_a, sensor_b):
	center_dist = math.sqrt((sensor_a[0]-sensor_b[0])**2 + (sensor_a[1]-sensor_b[1])**2)
	radius_dist = sensor_a[2] + sensor_b[2]
	if (radius_dist > center_dist):
		return True
	return False

def _touching_left(sensor):
	if sensor[0] - sensor[2] < 0:
		return True

def _touching_right(sensor):
	if sensor[0] + sensor[2] > 200:
		return True

def main():
	num = int(input())
	sensor_list = []
	for i in range(num):
		x,y,r = [int(val) for val in input().split(" ")]
		sensor_list.append((x,y,r))
	
	# Add the two ends to the unionfind/ sensor
	
	uFind = UnionFind(num+2)
	# Go from first to last
	# print(uFind.parents)
	for i in range(num):
		cur_sensor = sensor_list[i]

		# Check against all previous sensors
		for j in range(0, i): 
			prev_sensor = sensor_list[j]
			if _touching(cur_sensor, prev_sensor):
				uFind.union(i+1, j+1)

		# Check against left and right edges
		if _touching_left(cur_sensor):
			uFind.union(0, i+1)
		if _touching_right(cur_sensor):
			uFind.union(num+1, i+1)

		# See if the edges are connected
		# print(cur_sensor, " -> ", uFind.parents)
		if uFind.find(0) == uFind.find(num+1):
			print (i)
			break

if __name__ == "__main__":
	main()