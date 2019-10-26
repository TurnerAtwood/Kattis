/*	Turner Atwood
 *	9/17/19
 *	Sibice [1.3] https://open.kattis.com/problems/sibice
 *	Ad-hoc Trivial
 */
#include <iostream>

using namespace std;

int main() {
	int N,W,H;
	cin >> N >> W >> H;
	int diag = H*H + W*W; 
	int match;
	for (int i = 0; i < N; i++) {
		cin >> match;
		if (match*match <= diag) {
			cout << "DA\n";
		}
		else {
			cout << "NE\n";
		}
	}
}