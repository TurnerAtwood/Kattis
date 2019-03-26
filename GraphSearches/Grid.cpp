/*	Turner Atwood
 *	3/26/19
 *	Grid [3.0] : (https://open.kattis.com/problems/grid)
 *	BFS with edges between 'nonadjacent' matrix elements
 */

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

vector<int>* getNeighbors(int N, int M, int index, int jump);

int main() {
	// Setup grid
	int N,M;
	cin >> N >> M;
	int size = N*M;
	
	// Jumps is for weights, distances is visited map
	int jumps[size];
	int distances[size];
	
	// Clear newline
	string line;
	getline(cin, line);
	
	// Get the jumps
	for (int i = 0; i < N; i++) {
		getline(cin, line);
		for (int j = 0; j < M; j++) {
			jumps[i*M + j]     = line.at(j)-'0';
			distances[i*M + j] = -1;
		}
	}

	// Prepare the BFS
	distances[0] = 0;
	queue<int> bfsQueue;
	bfsQueue.push(0);

	// Run the BFS
	while (bfsQueue.size()) {
		// Access and remove next index
		int curPos = bfsQueue.front();
		bfsQueue.pop();

		// Early exit upon reaching the target
		if (curPos == size-1) {
			break;
		}

		// Visit all neighbors
		vector<int> neighbors = *getNeighbors(N, M, curPos, jumps[curPos]);
		for (vector<int>::iterator it = neighbors.begin(); it != neighbors.end(); it++) {
			// Never revisit a node
			if (distances[*it] != -1) {
				continue;
			}
			// Add to the queue and set the distance of the nighbor
			bfsQueue.push(*it);
			distances[*it] = distances[curPos] + 1;
		}
	}

	// Output
	cout << distances[size-1] << endl;
}

// Return the valid neighbors of a given index and jump length
vector<int>* getNeighbors(int N, int M, int index, int jump) {
	vector<int>* result = new vector<int>();
	int potential;
	// Up
	potential = index - jump*M;
	if (potential >= 0) {
		result->insert(result->end(),potential);
	}
	// Down
	potential = index + jump*M;
	if (potential < N*M) {
		result->insert(result->end(),potential);
	}
	// Left
	potential = index - jump;
	if (potential >= 0 && potential/M == index/M) {
		result->insert(result->end(),potential);
	}
	// Right
	potential = index + jump;
	if (potential < N*M && potential/M == index/M) {
		result->insert(result->end(),potential);
	}
	return result;
}