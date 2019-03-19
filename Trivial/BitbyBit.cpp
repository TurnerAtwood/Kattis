/*	Turner Atwood
 *	3/18/19
 *	Bit By Bit [3.0] : (https://open.kattis.com/problems/bitbybit)
 *	Ad-hoc - Use basic boolean logic
 */

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int N;
	string com;
	int a,b;
	cin >> N;
	while (N != 0) {
		// Initialize
		int bits[32];
		for (int i = 0; i < 32; i++) {
			bits[i] = '?';
		}

		// Run all commands
		for (int z = 0; z < N; z++) {
			cin >> com;
			cin >> a;
			if (com == "CLEAR") {
				bits[a] = '0';
			}
			else if (com == "SET") {
				bits[a] = '1';
			}
			// AND and OR have to account for ?'s
			else if (com == "OR") {
				cin >> b;
				if (bits[a] == '1' || bits[b] == '1') {
					bits[a] = '1';
				}
				else if (bits[a] == '?' || bits[b] == '?') {
					bits[a] = '?';
				}
				else {
					bits[a] = '0';
				}
			}
			// AND
			else {
				cin >> b;
				if (bits[a] == '0' || bits[b] == '0') {
					bits[a] = '0';
				}
				else if (bits[a] == '?' || bits[b] == '?') {
					bits[a] = '?';
				}
				else {
					bits[a] = '1';
				}
			}
		}

		// Print
		for (int i = 31; i >= 0; i--) {
			char out = bits[i];
			cout << out;
		}
		cout << endl;
		cin >> N;
	}
}