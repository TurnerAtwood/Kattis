/*	Turner Atwood
 *	10/30/19
 *	Postal Delivery [3.4] https://open.kattis.com/problems/delivery
 *	Ad-hoc : (Greedy) Start from the furthest stop and move in
 **	Treat the positive and negative locations separately
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct tup {
	int dist;
	int need;
};

// Given a sorted list (high -> low)
long cost(vector<tup> stops, int K) {
	int len = stops.size();
	if (len == 0) {
		return 0;
	}
	// Start at the furthest stop
	long cost = stops[0].dist;
	int onHand = K;
	int i = 0;
	while (i < len) {
		// If you can service stop i with the letters onHand, do it
		if (stops[i].need <= onHand) {
			onHand -= stops[i].need;
			stops[i].need = 0;

			// Move on - stop i was just finished
			i++;
		}
		else {
			// Drop off the letters you have
			stops[i].need -= onHand;

			// Come back to stop i with K letters
			onHand = K;
			cost += stops[i].dist;
		}	
	}

	// All of our trips were just one-way, so double the cost
	return cost*2;
}

int main() {
	// Input
	int N,K;
	cin >> N >> K;

	vector<tup> left;
	vector<tup> right;
	tup stop;

	// We will treat left and right the same, so make all negatives
	//	positives in their own list
	for (int i = 0; i < N; i++) {
		cin >> stop.dist >> stop.need;
		if (stop.dist < 0) {
			stop.dist *= -1;
			left.push_back(stop);
		}
		else {
			right.push_back(stop);
		}
	}
	// We need the list in descending order (of magnitude)
	reverse(right.begin(), right.end());

	cout << cost(left, K) + cost(right, K) << "\n";
}