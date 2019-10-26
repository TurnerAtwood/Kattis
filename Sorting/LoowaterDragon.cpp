/*	Turner Atwood
 *	8/20/19
 *	The Dragon of Loowater [3.3] https://open.kattis.com/problems/loowater
 *	Sort the lists then perform a linear scan
 */

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int n,m;
	cin >> n >> m;
	while (n != 0 && m !=0) {
		// Input
		int dragons[n];
		for (int i = 0; i < n; i++) {
			cin >> dragons[i];
		}
		sort(dragons, dragons+n);

		int knights[m];
		for (int i = 0; i < m; i++) {
			cin >> knights[i];
		}
		sort(knights, knights+m);

		int totalCost = 0;
		int currentDragon = 0;
		int currentKnight = 0;
		int dragonVal, knightVal;

		// Check all knights slaying dragons if possible
		while (currentDragon < n && currentKnight < m) {
			dragonVal = dragons[currentDragon];
			knightVal = knights[currentKnight];
			if (knightVal >= dragonVal) {
				totalCost += knightVal;
				currentDragon++;
			}
			currentKnight++;
		}

		// Output
		if (currentDragon == n) {
			cout << totalCost << "\n";
		}
		else {
			cout << "Loowater is doomed!\n";
		}

		// Check to see if there is another test case
		cin >> n >> m;
	}
	
}