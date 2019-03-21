/*	Turner Atwood
 *	3/21/19
 *	Cross Country [3.1] : (https://open.kattis.com/problems/crosscountry)
 *	Dijkstra's over a weighted, directed, connected graph
 */

#include <iostream>
#include <unordered_set>
#include <queue>

using namespace std;

// Used to couple intersections with distances in a priority queue
class Tuple {
	public:
	int index;
	int distance;

	void setInfo(int ind, int dist) {
		index = ind;
		distance = dist;	
	}
};

// Used to compare Tuples in the priority queue
bool operator<(const Tuple& a, const Tuple& b) {
	return b.distance < a.distance;
}

int main() {
	// Input
	int N,start,end;
	cin >> N >> start >> end;
	int distances[N*N];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> distances[N*i + j];
		}
	}

	// Dijkstra's data structures
	unordered_set<int> visited;
	priority_queue<Tuple> paths;

	// Use newPath to add tuples to the priority queue
	Tuple newPath;
	newPath.setInfo(start,0);
	paths.push(newPath);
	// Used to store info for the current intersection being visited
	int currentIndex;
	int currentDistance;
	while (paths.size()) {
		// Get the next intersection and visit it
		currentIndex = paths.top().index;
		currentDistance = paths.top().distance;
		paths.pop();
		visited.insert(currentIndex);

		// Check if this is the target
		if (currentIndex == end) {
			cout << currentDistance << endl;
			return 0;
		}

		// Add new paths to unvisited nodes to the queue
		for (int i = 0; i < N; i++) {
			if (visited.count(i)) {
				continue;
			}
			int newDistance = currentDistance + distances[N*currentIndex + i];
			newPath.setInfo(i, newDistance);
			paths.push(newPath);
		}

	}
}

