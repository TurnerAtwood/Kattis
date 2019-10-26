/*	Turner Atwood
 *	2/23/19
 *	An Industrial Spy [https://open.kattis.com/problems/industrialspy] : (3.3)
 *	Use a prime siev to get all of the primes from 1-10^8
 **	Then generate all of the possible numbers from the given digits
 **	Finally, check to see how many of the possibles are prime
 */
#include <iostream>
#include <unordered_set>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

static int MAX = 10000000;

int main() {
	// Sieve of Eratosthenes
	bool* sieve = new bool[MAX];
	sieve[0] = false;
	sieve[1] = false;
	for (int i = 2; i < MAX; i++) {
		sieve[i] = true;
	}

	for (int i = 2; i < 3180; i++) {
		if (sieve[i]) {
			int j = i*i; 
			while (j < MAX) {
				sieve[j] = false;
				j += i;
			}
		}
	}

	// INPUT
	int cases;
	cin >> cases;
	for (int z = 0; z < cases; z++) {
		// Get the digits into a vector of ints
		string line;
		cin >> line;
		vector<int> digits;
		int dig_num = line.size();
		for (int i = 0; i < dig_num; i++) {
			digits.push_back(line.at(i) - '0');
		}

		unordered_set<int> primes;
		unordered_set<int> checked;
		checked.insert(0);

		// Do a BFS over the digits, checking at each step if they are prime
		// <used list, number>
		queue<vector<int> > q;
		vector<int> cur;
		vector<int> neigh;
		int cur_num;
		int try_num;

		cur.push_back(0);
		q.push(cur);
		while (!q.empty()) {
			cur = q.front();
			q.pop();

			cur_num = cur.back();
			//cout << cur_num << endl;
			cur.pop_back();

			// Try to add all unused digits to the current number
			for (int i = 0; i < dig_num; i++) {
				// Index has been used
				if (find(cur.begin(), cur.end(), i) != cur.end()) {
					continue;
				}
				try_num = cur_num * 10 + digits[i];
				// Number has been checked already (on shorter path)
				if (checked.count(try_num)) {
					continue;
				}	

				checked.insert(try_num);
				if (sieve[try_num]) {
					primes.insert(try_num);
					//cout << try_num << endl;
				}

				neigh = cur;
				neigh.push_back(i);
				neigh.push_back(try_num);
				q.push(neigh);

			}
		}

		cout << primes.size() << endl;
	}
}