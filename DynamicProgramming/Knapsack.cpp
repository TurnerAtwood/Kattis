/*	Turner Atwood
 *	4/10/19
 *	Knapsack [5.7] : (https://open.kattis.com/problems/knapsack)
 *	0/1 Knapsack Problem: Use the memo array to get the list of items included
 */


#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

struct item {
	int value;
	int weight;
};

int main() {
	double Cdub;
	// Capacity, Number of items
	int C,N;
	// Continue until input runs out
	while (cin >> Cdub) {
		// We only need C as an integer since weights are all integers
		cin >> N;
		C = Cdub;

		// Store the items as tuples in an array (1-INDEXED)
		item items[N+1];

		item curItem;
		for (int i = 1; i < N+1; i++) {
			cin >> curItem.value;
			cin >> curItem.weight;
			items[i] = curItem;
		}

		// Memo Array: Item Index X Weight
		int memo[N+1][C+1];
		vector<int>* paths[N+1][C+1];
		for (int i = 0; i < C+1; i++) {
			memo[0][i] = 0;
			paths[0][i] = new vector<int>();
		}

		// Build the memo array
		int best = 0;
		for (int i = 1; i < N+1; i++) {
			curItem = items[i];
			for (int j = 0; j < C+1; j++) {
				if (curItem.weight > j) {
					memo[i][j] = memo[i-1][j];
				}
				else {
					memo[i][j] = max(memo[i-1][j], memo[i-1][j-curItem.weight]+curItem.value);
				}
			}
		}

		// Now traverse the memo array to get the included
		vector<int> included;
		// Start at the very bottom left
		int i = N;
		int j = C;
		while (i != 0 && j != 0) {
			// The ith item is included if (i,j) is different from (i-1,j)
			if (memo[i][j] != memo[i-1][j]) {
				included.push_back(i-1);
				// Remove the weight of this item from the capacity (j)
				j -= items[i].weight;
			}
			// Only consider item i once (at most)
			i--;
		}
		// Output
		cout << included.size() << "\n";
		sort(included.begin(), included.end());
		for (vector<int>::iterator it = included.begin(); it != included.end(); it++) {
			cout << *it << " ";
		}
		cout << "\n";
		
		// DEBUG - Printing
		/*
		cout << "   ";
		for (int j = 0; j < C+1; j++) {
			printf("%02d ", j);
		}
		cout << endl;
			
		for (int i = 0; i < N+1; i++) {
			printf("%02d ", i);
			for (int j = 0; j < C+1; j++) {
				printf("%02d ", memo[i][j]);
			}
			cout << endl;
		}

		cout << "--------------------\n";
		*/
	} //END OF TEST CASE
}