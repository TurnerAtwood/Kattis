/*	Turner Atwood
 *	10/24/19
 *	Virtual Friends [4.5] https://open.kattis.com/problems/virtualfriends
 *	Union-Find (With Rank)
 */

#include<iostream>
#include<unordered_set>
#include<unordered_map>

using namespace std;

string find(unordered_map<string,string> &parents, string a) {
	if (parents[a] == a) {
		return a;
	}

	parents[a] = find(parents,parents[a]);
	return parents[a];
}

int join(unordered_map<string,string> &parents,unordered_map<string,int> &sizes, string a, string b) {
	string p_a = find(parents,a);
	string p_b = find(parents,b);
	if (p_a == p_b) {
		return sizes[p_a];
	}

	sizes[p_a] += sizes[p_b];
	sizes[p_b] = sizes[p_a];
	parents[p_b] = p_a;
	return sizes[p_a];
}

int main() {
	int T;
	cin >> T;
	for (int z = 0; z < T; z++) {
		int F;
		cin >> F;

		unordered_map<string,string> parents;
		unordered_map<string,int> sizes;

		string a,b;
		for (int i = 0; i < F; i++) {
			cin >> a >> b;
			if (!parents.count(a)) {
				parents[a] = a;
				sizes[a] = 1;
			}
			if (!parents.count(b)) {
				parents[b] = b;
				sizes[b] = 1;
			}

			cout << join(parents,sizes,a,b) << "\n";
		}
	}
}