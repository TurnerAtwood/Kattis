/*	Turner Atwood
 *	11/1/19
 *	Train Sorting [5.0] https://open.kattis.com/problems/trainsorting
 *	DP : Push each car to the front AND back of all existing cars
 **		  then perform a LIS over all of them.
 **	This checks every car being added to the front OR the back.
 */

#include <iostream>

using namespace std;

int train() {
    // Faster Input (Not necessary)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Grab Input
    int N;
    cin >> N;

    // Trivial cases, returning early avoids headaches.
    if (N < 3) {
    	return N;
    }

    // Place each car to the front AND end of the existing car(s)
    //	Only 2*N-1 spots are needed, so we 1-index to make life easier
    int cars[2*N];
    for (int i = 0; i < N; i++) {
        cin >> cars[N+i];
        cars[N-i] = cars[N+i];
    }

    // Standard LIS [Longest Increasing Subsequence]
    int LIS[2*N];
    for (int i = 1; i < 2*N; i++) {
        LIS[i] = 1;
        for (int j = 1; j < i; j++) {
            if (cars[i] > cars[j]) {
                LIS[i] = max(LIS[i], LIS[j] + 1);
            }
        }
    }

    // Return the longest LIS
    int longest = 0;
    for (int i = 1; i < 2*N; i++) {
        longest = max(longest, LIS[i]);
    }
    return longest;
}

int main() {
    printf("%d\n", train());
}