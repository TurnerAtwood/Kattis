/*	Turner Atwood
 *	8/20/19
 *	Zebras and Ocelots [3.2] https://open.kattis.com/problems/zebrasocelots
 *	Ad-hoc : Binary with Ocelots as 1
 */

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	// Input
	int N;
	cin >> N;
	long count = 0;
	int digits[N];
	long power = 1;
	
	for (int i = 0; i < N; i++){
		char animal;
		cin >> animal;
		if (animal == 'O') {
			digits[i] = 1;
		}
		else {
			digits[i] = 0;
		}
	}

	for (int i = N-1; i >= 0; i--) {
		if (digits[i]) {
			count += power;
		}
		power *= 2;
	}
	cout << count << "\n";
}
