/*	Turner Atwood
 *	9/3/19
 *	Bumped! [4.4] https://open.kattis.com/problems/bumped
 *	Joining Two Dijkstra's from the start and end
 */

#include <iostream>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <vector>

using namespace std;

unordered_map<int,long> dijkstra (int s, int t, unordered_map<int,int>* cities);

class Tuple {
	public:
	int first;
	long second;

	Tuple() {
		first = -1;
		second = -1;
	}

	Tuple(int l, long d) {
		first = l;
		second = d;
	}
};

bool operator < (const Tuple& a, const Tuple& b) {
	return a.second > b.second;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);


	int n,m,f,s,t;
	cin >> n >> m >> f >> s >> t;

	//unordered_set<int> flights[n];
	int flights[2*f];
	unordered_map<int,int> cities[n];

	int a,b,c;
	// Get each road (they go both ways)
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> c;
		(cities[a])[b] = c;
		(cities[b])[a] = c;
	}

	// Get each flight
	for (int i = 0; i < f; i++) {
		cin >> a >> b;
		flights[2*i] = a;
		flights[2*i+1] = b;
		//flights[a].insert(b);
	}

	// Forwards AND Backwards
	unordered_map<int,long> forwards = dijkstra(s, t, cities);
	unordered_map<int,long> backwards = dijkstra(t, s, cities);
	
	// Check all flights
	long best = 100000000000000000;
	if (forwards.count(t)) {
		best = forwards[t];
	}

	long potential;
	for (int i = 0; i < f; i++) {
		a = flights[2*i];
		b = flights[2*i+1];

		potential = 100000000000000000;
		if (forwards.count(a) && backwards.count(b)) {
			potential = forwards[a] + backwards[b];
		}

		//printf("%d %d: %ld\n", a, b, potential);

		if (potential < best) {
			best = potential;
		}
	}

	cout << best << "\n";

}

unordered_map<int,long> dijkstra (int s, int t, unordered_map<int,int>* cities) {
	unordered_map<int,long> visited;

	priority_queue<Tuple> q;
	Tuple current = Tuple(s, 0);
	Tuple other;
	q.push(current);

	while (q.size()) {
		current = q.top();
		q.pop();

		if (visited.count(current.first)) {
			continue;
		}

		visited[current.first] = current.second;

		for (unordered_map<int,int>::iterator it = cities[current.first].begin(); it != cities[current.first].end(); it++) {
			if (visited.count(it->first)) {
				continue;
			}

			other = Tuple(it->first, current.second + it->second);
			q.push(other);
		}
	} // End of p_queue

	return visited;
}