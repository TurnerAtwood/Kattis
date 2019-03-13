/*	Turner Atwood
 *	3//19
 *	Disastrous Downtime [3.3] : (https://open.kattis.com/problems/downtime)
 *	Each time slot has a start time and and end time
 **	All of these endpoints will be SORTED in a list then scanned linearly
 **	A counter can be kept to tell the largest overlapping subsequence
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
 
// Even endpoints are starts and odd ones are endpoints
int main() {
 	vector<int> endpoints;
 	int N,K;
 	cin >> N >> K;
 	int time;
 	// Read input - each slot is 999 long
 	for (int i = 0; i < N; i++) {
 		cin >> time;
 		endpoints.insert(endpoints.end(), time*2);
 		endpoints.insert(endpoints.end(), time*2+1999); // [0,999] -> [0,1999]
 	}

 	// Sort the endpoints
 	sort(endpoints.begin(), endpoints.end());

 	// Track how high the load gets on the server
 	int currentCount = 0;
 	int bestCount = 0;
 	for(vector<int>::iterator it = endpoints.begin(); it != endpoints.end(); it++) {
 		int current = *it;
 		// +1 if start point, -1 if an endpoint
 		currentCount += (current%2)*-2 + 1;
 		bestCount = max(bestCount, currentCount);
 	}

 	// Account for the server load, then output
 	cout << ceil(bestCount*1.0/K) << endl;
}