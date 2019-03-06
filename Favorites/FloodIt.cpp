/*	Turner Atwood
 *	3/6/19
 *	Flood-It [5.2] : (https://open.kattis.com/problems/floodit)
 *	Union-Find to join already connected elements
 **	Use adjacency lists to tell which disjoint sets are neighbors
 **	Start at the top left and incorperate all neighbors of color i,
 ** where color i increases the number of elements in visited by the most
 */

#include <vector>
#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int find(int* graph, int* sizes, int a);
void unify(int* graph, int* sizes, int a, int b);
void dumpArray(int* arr, int N);

int main() {
	int cases;
	cin >> cases;
	// Each Individual Case
	for (int z = 0; z < cases; z++) {
		// Throw everything into a unionfind
		int N;
		cin >> N;
		int colors[N*N];
		int parents[N*N];
		int sizes[N*N];
		// Initialize all data structures
		for (int i = 0; i < N*N; i++) {
			parents[i] = i;
			sizes[i] = 1;
		}
		// Grab the colors from the input
		for (int i = 0; i < N; i++) {
			string line;
			cin >> line;
			for (int j = 0; j < N; j++) {
				colors[i*N+j] = line.at(j) - '0';
			}
		}
		// Try to union every elem to the right and below
		// This goes backwards to make the R.E.'s as small as possible
		for (int i = N*N-1; i >= 0; i--) {
			// RIGHT 
			if (i+1 < N*N && (i+1)/N == i/N && colors[i] == colors[i+1]) {
				unify(parents, sizes, i, i+1);
			}
			// DOWN
			if (i+N < N*N && colors[i] == colors[i+N]) {
				unify(parents, sizes, i, i+N);
			}
		}

		// Find on everything to compress the entire graph
		// Now, same parent <==> same group
		unordered_map<int, unordered_set<int>*>* neighbors = new unordered_map<int, unordered_set<int>*>();
		for (int i = 0; i < N*N; i++) {
			int parent = find(parents, sizes, i);
			if (neighbors->count(parent) != 0) {
				continue;
			}
			pair<int,unordered_set<int>*> myPair (parent, new unordered_set<int>());
			neighbors->insert(myPair);
		}
		
		// Build the adjacency lists for each group
		// neighbors have at least one adjacent pair
		// This graph is undirected	
		for (int i = 0; i < N*N; i++) {
			int p = parents[i];
			unordered_set<int>* here = neighbors->at(p);
			// RIGHT
			if (i+1 < N*N && (i+1)/N == i/N && colors[i] != colors[i+1]) {
				unordered_set<int>* there = neighbors->at(parents[i+1]);
				here->insert(parents[i+1]);
				there->insert(p);
			}
			// DOWN
			if (i+N < N*N && colors[i] != colors[i+N]) {
				unordered_set<int>* there = neighbors->at(parents[i+N]);
				here->insert(parents[i+N]);
				there->insert(p);
			}
		}

		// Store neighbors already incorperated
		unordered_set<int>* visited = new unordered_set<int>();
		// Store available neighbors for each color (1-6)
		unordered_set<int>* choices[7];
		for (int i = 0; i <= 6; i++) {
			choices[i] = new unordered_set<int>();
		}

		// Add group 0 to visited and its neighbors to choices
		visited->insert(parents[0]);
		unordered_set<int>* adj = neighbors->at(parents[0]);
		for (unordered_set<int>::iterator it = adj->begin(); it != adj->end(); it++) {
			int neigh = *it;
			int val = colors[neigh];
			choices[val]->insert(neigh);
		}

		// These variables hold the results
		int resultTotal = 0;
		int resultChoices[7] = {0};

		// Make choices until all elements have been chosen
		// This is the actual SEARCH ALGORITHM
		while (visited->size() < neighbors->size()) {
			int bestScore = 0;
			int bestColor = 0;
			// Try each color, see which one has the most elements
			for (int i = 1; i <= 6; i++) {
				// Find the size of all groups currently reachable with COLOR == i
				int curScore = 0;
				unordered_set<int>* iChoices = choices[i];
				for (unordered_set<int>::iterator it = iChoices->begin(); it != iChoices->end(); it++) {
					curScore += sizes[*it];
				}

				// Compare COLOR i's score to the best so far
				if (curScore > bestScore) {
					bestScore = curScore;
					bestColor = i;
				}
			}

			// Save the current choice in results
			resultTotal += 1;
			resultChoices[bestColor] += 1;

			// Add the groups in the choice to visited and their
			// (new) neighbors to the choices
			unordered_set<int>* newAdditions = choices[bestColor];
			for (unordered_set<int>::iterator it = newAdditions->begin(); it != newAdditions->end(); it++) {
				visited->insert(*it);
				unordered_set<int>* potChoices = neighbors->at(*it);
				for (unordered_set<int>::iterator nit = potChoices->begin(); nit != potChoices->end(); nit++) {
					// Cannot add a group as a choice if it has been visited
					if (visited->count(*nit) != 0) {
						continue;
					}
					// Add the new group to choices under the appropriate color
					int nitColor = colors[*nit];
					choices[nitColor]->insert(*nit);
				}
			}

			// Reset the selected choice since they were all visited
			choices[bestColor] = new unordered_set<int>();
		}
		// Print results
		cout << resultTotal << endl;
		for (int i = 1; i < 6; i++) {
			cout << resultChoices[i] << " ";
		}
		cout << resultChoices[6] << endl;
	}
}

int find(int* graph, int* sizes, int a) {
	if (graph[a] == a) {
		return a;
	}
	graph[a] = find(graph, sizes, graph[a]);
	sizes[a]= sizes[graph[a]];
	return graph[a];
}

// Currently keeping track of sizes in a different array
void unify(int* graph, int* sizes, int a, int b) {
	int p_a = find(graph, sizes, a);
	int p_b = find(graph, sizes, b);
	if (p_a == p_b) {
		return;
	}
	if (p_a < p_b) {
		graph[p_b] = p_a;
	}
	else {
		graph[p_a] = p_b;
	}
	sizes[p_a] += sizes[p_b];
	sizes[p_b]  = sizes[p_a];
}

// For debug purposes
void dumpArray(int* arr, int N) {
	cout << "ARRAY:\n";
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			printf("%03d ", arr[i*N+j]);
		}
		cout << endl;
	}
}