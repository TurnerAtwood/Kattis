/*	Turner Atwood
 *	10/20/19
 *	Where's My Internet? [4.1] https://open.kattis.com/problems/wheresmyinternet
 *	Unionfind : Much faster/cleaner than before
 */

#include<iostream>
#include<unordered_map>
#include<unordered_set>

using namespace std;

int find(int* parents, int a) {
	int p_a = parents[a];
	if (p_a == a) {
		return a;
	}

	int best = find(parents, p_a);
	parents[a] = best;
	return best;
}

void join(int* parents, int a, int b) {
	int p_a = find(parents, a);
	int p_b = find(parents, b);
	if (p_a < p_b) {
		parents[p_b] = parents[p_a];
	}
	else {
		parents[p_a] = parents[p_b];
	}
}

int main() {
	int N,M;
	cin >> N >> M;

	int parents[N];
	for (int i = 0; i < N; i++) {
		parents[i] = i;
	}

	int a,b;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		join(parents, a-1,b-1);
	}

	for (int i = N-1; i >= 0; i--) {
		find(parents,i);
	}

	int bad = 0;
	for (int i = 0; i < N; i++) {
		if (parents[i] != parents[0]) {
			bad++;
			cout << i+1 << "\n";
		}
	}

	if (bad == 0) {
		cout << "Connected\n";
	}

}