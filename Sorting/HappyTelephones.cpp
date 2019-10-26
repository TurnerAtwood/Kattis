/*	Turner Atwood
 *	10/15/19
 *	Happy Telephones [2.7] https://open.kattis.com/problems/telephones
 *	Sort the Start/End Times and perform Binary Searches
 */
#include <iostream>
#include <algorithm>

using namespace std;

// Returns the index of max element less than target in (sorted) array
int binarySearch(int target, int* array, int size) {
	int a = 0;
	int b = size-1;
	int m, m_v;
	while (b-a > 1) {
		m = (a + b)/2;
		m_v = array[m];
		if (m_v < target) {
			a = m;
		}
		else {
			b = m;
		}
	}

	if (target > array[b]) {
		return b+1;
	}
	if (target > array[a]) {
		return a+1;
	}
	return 0;
}

int main() {
	int N = 1;
	int M = 1;
	while (true) {
		// Case input
		cin >> N >> M;
		if (N == 0 && M == 0) {
			break;
		}

		// Calls Input
		int* starts = new int[N];
		int* ends = new int[N];

		int source, destination, start, duration;
		for (int i = 0; i < N; i++) {
			cin >> source >> destination >> start >> duration;
			starts[i] = start;
			ends[i] = start + duration;
		}

		sort(starts, starts + N);
		sort(ends, ends + N);
		
		// Intervals Input/Output
		for (int i = 0; i < M; i++) {
			cin >> start >> duration;
			int end = start + duration;
			// Active during a call = started by (end) - ended by (start)
			int active = binarySearch(end, starts, N) - binarySearch(start+1, ends, N);
			cout << active << "\n";
		}
	}	

}

