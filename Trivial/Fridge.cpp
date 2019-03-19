/*	Turner Atwood
 *	3/18/19
 *	Fridge [3.3] : (https://open.kattis.com/problems/fridge)
 *	Math - Find the digit with the lowest frequency
 */

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
int main() {
	// Initialize storage
	string input;
	int N;
	cin >> input;
	N = input.size();
	int frequencies[10] = {0};

	// Count the frequencies (0 is used 1 less time than others)
	frequencies[0]++;
	for (int i = 0; i < N; i++) {
		frequencies[input.at(i)-'0']++;
	}

	// Find the minimum of the frequencies
	int minVal = frequencies[0];
	int minDigit = 0;
	for (int i = 1; i < 10; i++) {
		if (frequencies[i] < minVal) {
			minVal = frequencies[i];
			minDigit = i;
		}
	}

	// Put a 1 on the front if zero
	if (minDigit == 0) {
		cout << 1;
		minVal--;
	}
	// Finish the output
	for (int i = 0; i < minVal+1; i++) {
		cout << minDigit;
	}
	cout << endl;
}