/*	Turner Atwood
 *	11/1/18
 *	Milestone Counter [3.3] (https://open.kattis.com/problems/milestones)
 *	Ad-hoc : Trying to get back into c++
 */

#include<iostream>
#include<vector>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int main() {
	// Input
	int M,N;
	cin >> M;
	cin >> N;
	
	long timeDiffs[M-1];
	long distances[N];
	long distDiffs[N-1];
	long prev,curr;
	
	// Get the differences between consecutive times and distances
	cin >> prev;
	M--;
	for (int i = 0; i < M; i++) {
		cin >> curr;
		timeDiffs[i] = curr - prev;
		prev = curr;
	}
	cin >> prev;

	// Must also save distances for output
	distances[0] = prev;
	N--;
	for (int i = 0; i < N; i++) {
		cin >> curr;
		distDiffs[i] = curr - prev;
		prev = curr;
		distances[i+1] = prev;
	}

	// Try starting at each marker
	vector<int> result;
	for (int i = 0; i < N+1-M; i++) {
		// The factor*time must match the next M distances to work
		float factor = distDiffs[i]*1.0/timeDiffs[0];
		bool good = true;
		for (int j = 1; j < M; j++) {
			if (distDiffs[i+j] != factor*timeDiffs[j]) {
				good = false;
				break;
			}
		}
		if (good)
			result.push_back(distances[i+1]-distances[i]);
	}

	// Sort the results and remove non-unique elements
	sort(result.begin(), result.end());
	vector<int>::iterator it;
	it = unique(result.begin(), result.end());
	result.resize(distance(result.begin(), it));

	// Output
	cout << result.size() << endl;
	for (int i = 0; i < result.size(); i++)
		cout << result.at(i) << " ";
	cout << endl;
}

