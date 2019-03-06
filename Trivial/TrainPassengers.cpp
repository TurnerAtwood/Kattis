/*	Turner Atwood
 *	3/6/19
 *	Train Passengers [2.6] : (https://open.kattis.com/problems/trainpassengers)
 *	Ad-hoc - check status of variable each iteration
 */

#include <iostream>
#include <vector>

using namespace std;

int main() {
	int capacity, stations;
	cin >> capacity >> stations;
	int onboard = 0;
	bool possible = true;
	for (int z = 0; z < stations; z++) {
		// Input
		int off, on, stay;
		cin >> off >> on >> stay;

		// Onboard cannot dip below 0 or go above capacity
		onboard -= off;
		if (onboard < 0) {
			possible = false;
		}
		onboard += on;
		if (onboard > capacity) {
			possible = false;
		}

		// No passenger should wait if the train is not full
		if (stay > 0 && onboard < capacity) {
			possible = false;
		}

		//Early exit
		if (!possible) {
			break;
		}
	}
	// The train should be empty at the end
	if (onboard != 0) {
		possible = false;
	}

	if (possible) {
		printf("possible\n");
	}
	else {
		printf("impossible\n");
	}

}