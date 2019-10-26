/*	Turner Atwood
 *	10/13/18
 *	CD [4.2] https://open.kattis.com/problems/cd
 *	Ad-hoc using a set
 */

using namespace std;

#include <iostream>
#include <unordered_set>

int main() {
	int N,M;
	cin >> N >> M; 
	unordered_set<int> jack;
	int CD;
	while(N != 0 and M != 0) {
		int count = 0;
		
		jack = unordered_set<int>();
		for (int i = 0; i < N; i ++) {
			cin >> CD;
			jack.insert(CD);
		}
		
		for (int i = 0; i < N; i ++) {
			cin >> CD;
			if (jack.count(CD)) {
				count++;
			}
		}
		cout << count << endl;

		cin >> N >> M;
	}
}