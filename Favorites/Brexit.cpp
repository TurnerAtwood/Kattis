/*	Turner Atwood
 *	10/27/19
 *	Brexit [3.5] https://open.kattis.com/problems/brexit
 *	BFS : Nodes are only explored after being visited
 **	a certain amount of times (Normal is exactly once).
 */

#include <iostream>
#include <vector>
#include <queue>
#include <math.h>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	
	int C,P,X,L;
	cin >> C >> P >> X >> L;

	// Exit early if possible
	if (X == L) {
		cout << "leave\n";
		return 0;
	}

	// Grab the trade partners
	unordered_set<int> neighbors[C+1];
	int A,B;
	for (int i = 0; i < P; i++) {
		cin >> A >> B;
		neighbors[A].insert(B);
		neighbors[B].insert(A);
	}

	// A Country leaves after at least half of its neighbors leave
	int resistances[C+1];
	for (int i = 1; i <= C; i++) {
		resistances[i] = ceil(neighbors[i].size()/2.0);
	}
	resistances[L] = 0;

	// BFS
	queue<int> q;
	q.push(L);
	int cur;

	while (!q.empty()) {
		cur = q.front();
		q.pop();

		unordered_set<int> cNeighs = neighbors[cur];
		for (unordered_set<int>::iterator it = cNeighs.begin(); it != cNeighs.end(); it++) {
			resistances[*it]--;
			// Only visit nodes the first time we know they will leave
			if (resistances[*it] == 0) {
				// Another early exit
				if (*it == X) {
					cout << "leave\n";
					return 0;
				}
				q.push(*it);
			}
		}
	}

	cout << "stay\n";
}
