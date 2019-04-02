/*	Turner Atwood
 *	4/2/19	
 *	Single Source Shortest Path, Non-negative Weights [3.5] : (https://open.kattis.com/problems/shortestpath1)
 *	Straightforward Dikstra's
 */

#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

// Tuples used to store vertices during Dijkstra's
struct tup {
	long pos;
	long dist;
};

bool operator< (const tup &t1, const tup &t2) {
	return t1.dist > t2.dist;
}

int main() {
	long N,M,Q,S;
	cin >> N >> M >> Q >> S;
	bool first = true;
	while (N != 0 || M != 0 || Q != 0 || S != 0) {
		// Print newline if not the first testcase
		if (!first) {
			cout << endl;
		}
		first = false;

		// Init the edge maps
		unordered_map<long,long> neighbors[N];

		// Get the edges
		long U,V,W;
		for (long i = 0; i < M; i++) {
			cin >> U >> V >> W;
			// If there is already a path from U -> V, choose the shorter one
			if (neighbors[U].count(V) != 0) {
				long oldVal = (neighbors[U])[V];
				if (W < oldVal) {
					(neighbors[U])[V] = W;
				}
			}
			// If no path already exists, make a new one
			else {
				(neighbors[U])[V] = W;
			}
		}

		// For visited set and final distances array
		unordered_map<long,long>* distances = new unordered_map<long,long>();
		// tup used to insert into pq
		tup tmpTuple;

		// Set up dijkstra's
		priority_queue<tup> pq;
		tmpTuple.pos = S;
		tmpTuple.dist = 0;
		pq.push(tmpTuple);

		// Dijkstra's
		while (pq.size() != 0) {
			// Get the next node and visit it
			long curIndex = pq.top().pos;
			long curDist = pq.top().dist;
			pq.pop();

			// Never revisit a node
			if ((*distances).count(curIndex) != 0) {
				continue;
			}
			(*distances)[curIndex] = curDist;

			// Add all unvisited neighbors from the current node to the queue
			unordered_map<long,long> curNeighbors = (neighbors[curIndex]);
			for (unordered_map<long,long>::iterator it = curNeighbors.begin(); it != curNeighbors.end(); it++) {
				// No need to add visited nodes to the 
				if (distances->count(it->first)) {
					continue;
				}
				tmpTuple.pos = it->first;
				tmpTuple.dist = curDist + it->second;
				pq.push(tmpTuple);
			}
		}

		// Handle Queries
		long destination;
		for (long i = 0; i < Q; i++) {
			cin >> destination;
			if (distances->count(destination)) {
				cout << (*distances)[destination] << endl;
			}
			else {
				cout << "Impossible\n";
			}
		}

		// Get the next test case
		cin >> N >> M >> Q >> S;
	}
}