/*	Turner Atwood
 *	10/20/19
 *	Cracking The Safe [3.3] https://open.kattis.com/problems/safe
 *	BFS/Brute-Force every possible combination
 */

#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

vector<int> reverse(vector<int> keys, int index) {
	for (int i = 0; i < 3; i++) {
		keys[(index/3)*3 + i]--;
		keys[(index%3) + 3*i]--;
	}
	keys[index]++;

	for(int i = 0; i < 9; i++) {
		keys[i] = (keys[i]+4)%4;
	}

	return keys;
}

int main() {
	vector<int> allZeros;
	for (int i = 0; i < 9; i++) {
		allZeros.push_back(0);
	}

	map<vector<int>, int> dists;
	dists[allZeros] = 0;
	queue<vector<int> > q;
	q.push(allZeros);

	// Calculate all possible combos
	vector<int> me;
	vector<int> you;
	while (!q.empty()) {
		me = q.front();
		q.pop();

		for (int i = 0; i < 9; i++) {
			you = reverse(me, i);
			if (!dists.count(you)) {
				dists[you] = dists[me] + 1;
				q.push(you);
			}
		}
	}

	// GET INPUT
	vector<int> inp;
	int key = 0;
	for (int i = 0; i < 9; i++) {
		cin >> key;
		inp.push_back(key);
	}

	// OUTPUT
	if (dists.count(inp)) {
		cout << dists[inp] << endl;
	}
	else {
		cout << "-1\n";
	}

}