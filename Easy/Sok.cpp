/*	Turner Atwood
	12/24/18
	Sok [1.6] (https://open.kattis.com/problems/sok)
	Trivial Math
*/

#include <iostream>

#define SIZE 3
#define MAX 10000
using namespace std;

int main() {
	// [orange, apple, pineapple] for each array
	float have[SIZE];	// Amount bought
	float need[SIZE];	// Amount needed
	float make[SIZE];	// Amount can make

	// Half of Input
	for(int i = 0; i < SIZE; i++) {
		cin >> have[i];
	}

	float lowest = MAX;
	for(int i = 0; i < SIZE; i++) {
		// Get Needed
		cin >> need[i];
		// Calculate amount makeable
		make[i] = have[i] / need[i];
		// Keep track of the minimum makeable
		lowest = min(lowest, make[i]);
	}

	// Final Calculation and Output
	for(int i = 0; i < SIZE; i++) {
		printf("%f ", have[i] - need[i] * lowest);
	}
	cout << "\n";

	return 0;
}