/*	Turner Atwood
 *	10/24/19
 *	Kastenlauf [4.0] https://open.kattis.com/problems/kastenlauf
 *	BFS : Cleaner/Faster than before
 */

#include <iostream>
#include <stack>
#include <unordered_set>

using namespace std;

static const int MAX = 1000;

int main() {
	int T,N;
	cin >> T;
	for (int z = 0; z < T; z++) {
		cin >> N;
		N += 2;
		
		int xCoords[N]; 
		int yCoords[N]; 
		for (int i = 0; i < N; i++) {
			cin >> xCoords[i];
			cin >> yCoords[i];
		}

		// Make adjacency Lists
		unordered_set<int> neighs[N];
		int curX,curY;
		for (int i = 0; i < N; i++) {
			curX = xCoords[i];
			curY = yCoords[i];
			for (int j = i+1; j < N; j++) {
				if (abs(curX - xCoords[j]) + abs(curY - yCoords[j]) <= MAX) {
					neighs[i].insert(j);
					neighs[j].insert(i);
				}
			}
		}

		// DFS
		unordered_set<int> visited;
		stack<int> stak;
		stak.push(0);
		while(!stak.empty()) {
			int cur = stak.top();
			stak.pop();


			if (visited.count(cur)) {
				continue;
			}
			visited.insert(cur);

			if (cur == N-1) {
				break;
			}

			unordered_set<int> curNeigh = neighs[cur];
			for (unordered_set<int>::iterator it = curNeigh.begin(); it != curNeigh.end(); it++) {
				if (!visited.count(*it)) {
					stak.push(*it);
				}
			}
		}

		if (visited.count(N-1)) {
			cout << "happy\n";
		}
		else {
			cout << "sad\n";
		}
	}

}