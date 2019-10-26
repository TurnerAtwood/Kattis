/*	Turner Atwood
 *	8/21/19
 *	Geppetto [3.5] https://open.kattis.com/problems/geppetto
 *	Ad-hoc : Brute Force
 */

#include <iostream>
#include <math.h>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
	int N,M;
	cin >> N >> M;
	unordered_set<int> collisions[N];
	int a,b;
	for (int i = 0; i < M; i++) {
		cin >> a >> b;
		a--;
		b--;
		if (a < b) {
			collisions[a].insert(b);
		}
		else {
			collisions[b].insert(a);
		}	
	}

	// Try every combination of toppings
	int count = 0;
	int comboCount = pow(2,N);
	int digits[N];
	for (int i = 0; i < comboCount; i++) {
		// Generate the binary
		int k = i;
		for (int j = 0; j < N; j++) {
			digits[N-1-j] = k%2;
			k /= 2;
		}

		bool good = true;
		for (int j = 0; j < N; j++) {
			if (!digits[j]) {
				continue;
			}
			for (unordered_set<int>::iterator it = collisions[j].begin(); it != collisions[j].end(); it++) {
				if (digits[*it]) {
					good = false;
					break;
				}
			}
			if (!good) {
				break;
			}
		}

		if (good) {
			count++;
		}
	}

	cout << count << "\n";
}
