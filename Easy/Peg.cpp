/*	Turner Atwood
 *	3/5/19
 *	Peg [1.8] : (https://open.kattis.com/problems/peg)
 *	Trivial BFS of length 1 from each point
 **	Meant for practice in c++
 */

#include <iostream>

using namespace std;

int main() {
	// read in oddly-shaped board (0 --> wall)
	int board[7][7] = {{0}};
	string line;
	for (int i = 0; i < 7; i++) {
		cin>>line;
		int start = 0;
		if (line.size() == 3) {
			start = 2;
		}
		for (int j = 0; j < line.size(); j++) {
			// Negative --> open spot
			board[i][start+j] = line.at(j) - 78;
		}
	}

	int count = 0;
	// Try every spot up/right/down/left
	int x[] = {0,-1,0,1};
	int y[] = {-1,0,1,0};
	for (int i = 0; i < 7; i++) {
		for (int j = 0; j < 7; j++) {
			// Try peg at [i][j]
			if (board[i][j] > 0) {
				for (int k = 0; k < 4; k++) {
					// Final destination
					int dest_y = i + 2*y[k];
					int dest_x = j + 2*x[k];
					// Spot to be jumped over
					int jmp_y = i + y[k];
					int jmp_x = j + x[k];

					// Make sure the jump would be in bounds
					if (dest_x > 6 || dest_x < 0 || dest_y > 6 || dest_y < 0) {
						continue;
					}
					// Make sure there is a peg in the jmp spot and dest is .(< 0)
					if (board[jmp_y][jmp_x] > 0 && board[dest_y][dest_x] < 0) {
						count++;
					}
				}
			}
		}
	}
	// Print result
	cout << count << endl;
}