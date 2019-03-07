/*	Turner Atwood
 *	3/7/19
 *	Misa [2.1] : (https://open.kattis.com/problems/misa)
 *	BFS of length 1 from every point
 **	Challenge: checking 8 neighbors of an element in a matrix
 */

#include <iostream>
#include <set>

using namespace std;

int shakes(int start, int graph[], int R, int S);

int main() {
	// Get input and build the graph
	int R,S;
	cin >> R >> S;
	// 1 -> Person, 0 -> No person
	int size = R*S;
	int graph[size];
	for (int i = 0; i < R; i++) {
		string line;
		cin >> line;
		for (int j = 0; j < S; j++) {
			if (line.at(j) == 'o') {
				graph[i*S+j] = 1;
			}
			else {
				graph[i*S+j] = 0;	
			}
		}
	}

	// 
	int bestEmpty = 0;
	int totalShakes = 0;
	for (int i = 0; i < R*S; i++) {
		int possibleShakes = shakes(i, graph, R, S);
		// If there is already a person in the spot
		if (graph[i] == 1) {
			totalShakes += possibleShakes;
		}
		// Otherwise, check if this is the best empty spot so far
		else if (possibleShakes > bestEmpty) {
			bestEmpty = possibleShakes;
		}
	}
	// Counted every existing shake twice
	totalShakes /= 2;
	// Add in the spot we sat in (if any)
	totalShakes += bestEmpty;
	cout << totalShakes << endl;
}

// Try all 8 directions for a given start in graph (return # of adjacent 1's)
int shakes(int start, int graph[], int R, int S) {
	set<int>* neighbors = new set<int>();
	int spot;
	// Left/Right
	for (int i = -1; i < 2; i++) {
		// Up/Down
		for (int j = -1; j < 2; j++) {
			spot = start + j*S + i;
			// Make sure the spot is non-trivial, in-bounds, and not empty
			if ((i == 0 && j == 0) || spot < 0 || spot >= R*S || graph[spot] == 0) {
				continue;
			}
			// Actual row must be adjacent (or same) row
			// This accounts for the edges of the graph (where +/- 1 changes the row)
			if (spot/S - start/S != j) {
				continue;
			}
			neighbors->insert(spot);
		}
	}
	return neighbors->size();
}