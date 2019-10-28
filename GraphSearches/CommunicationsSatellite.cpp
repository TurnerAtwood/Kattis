/*	Turner Atwood
 *	10/27/19
 *	Communications Satellite [3.6] https://open.kattis.com/problems/communicationssatellite
 *	Minimum Spanning Tree : Prim's Algorithm
 */

#include <iostream> 
#include <cmath>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>

using namespace std;

// Tuple used for Prim's
struct tup {
	int index;
	double cost;
};

bool operator<(const tup& a, const tup& b) {
	return a.cost > b.cost;
}

// Cost is the distance minus the radii
double getCost(int ax, int ay, int ar, int bx, int by, int br) {
	double result = sqrt((ax-bx)*(ax-bx) + (ay-by)*(ay-by));
	result = result - ar - br;
	return result;
}

int main() {
	cout.precision(10);
	int N;
	cin >> N;

	int dx[N];
	int dy[N];
	int dr[N];

	for (int i = 0; i < N; i++) {
		cin >> dx[i] >> dy[i] >> dr[i];
	}

	// Adjacency Matrix of Costs
	double costs[N][N];
	for (int i = 0; i < N-1; i++) {
		for (int j = i+1; j < N; j++) {
			costs[i][j] = getCost(dx[i], dy[i], dr[i], dx[j], dy[j], dr[j]);
			costs[j][i] = costs[i][j];
		}
	}

	unordered_set<int> unused;
	for (int i = 0; i < N; i++) {
		unused.insert(i);
	}
	priority_queue<tup> pq;
	double total = 0;

	tup cur;
	cur.index = 0;
	cur.cost = 0;
	pq.push(cur);

	// Use Prim's
	while(!pq.empty()) {
		cur = pq.top();
		pq.pop();

		if (!unused.count(cur.index)) {
			continue;
		}

		total += cur.cost;
		unused.erase(cur.index);

		for (unordered_set<int>::iterator it = unused.begin(); it != unused.end(); it++) {
			tup newTup;
			newTup.index = *it;
			newTup.cost = costs[cur.index][*it];
			pq.push(newTup);
		}
	}

	cout << total << "\n";
}