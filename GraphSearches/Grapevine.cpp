/*	Turner Atwood
 *	10/17/19
 *	Grapevine [6.9] https://open.kattis.com/problems/grapevine
 *	BFS - nodes may require multiple incoming edges
 */

#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n,m,d;
	cin >> n >> m >> d;

	unordered_map<string,int> skeptics;
	unordered_map<string, unordered_set<string> > friends;

	string name;
	string name2;
	int skep;
	for (int i = 0; i < n; i++) {
		cin >> name >> skep;
		skeptics[name] = skep; 
	}

	for (int i = 0; i < m; i++) {
		cin >> name >> name2;
		friends[name].insert(name2);
		friends[name2].insert(name);
	}

	// Perform a ~BFS
	cin >> name;
	unordered_map<string,int> timesHeard;
	unordered_map<string,int> dayHeard;
	unordered_set<string> talked;
	queue<string> q;
	q.push(name);
	dayHeard[name] = 0;
	string current;
	while (!q.empty()) {
		current = q.front();
		q.pop();

		// Ignore those not ready to talk
		if (timesHeard[current] < skeptics[current] || talked.count(current)) {
			continue;
		}

		// Nobody talks after the allowed day
		if (dayHeard[current] == d) {
			continue;
		}

		talked.insert(current);

		unordered_set<string> curFriends = friends[current];
		for (unordered_set<string>::iterator it = curFriends.begin(); it != curFriends.end(); it++) {
			if (talked.count(*it)) {
				continue;
			}

			if (!timesHeard.count(*it)) {
				timesHeard[*it] = 0;
			}
			timesHeard[*it]++;
			dayHeard[*it] = dayHeard[current] + 1;
			
			q.push(*it);
		}
	}

	cout << timesHeard.size() - 1 << endl;
}