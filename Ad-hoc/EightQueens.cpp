/*	Turner Atwood
 *	10/17/19
 *	Eight Queens [3.3] https://open.kattis.com/problems/8queens
 *	Ad-hoc : Careful 2D-Matrix Traversal
 */

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int board[8][8];
	// INPUT
	string line;
	for (int i = 0; i < 8; i++) {
		cin >> line;
		for (int j = 0; j < 8; j++) {
			if (line[j] == '*') {
				board[i][j] = 1;
			}
			else {
				board[i][j] = 0;
			}
		}
	}

	bool valid = true;

	// SIDE/UP
	int count;
	for (int i = 0; i < 8; i++) {
		count = 0;
		for (int j = 0; j < 8; j++) {
			count += board[i][j];
			count += board[j][i];
		}
		if (count != 2) {
			valid = false;
		}
	}

	//DIAG
	for (int i = 0; i < 8; i++) {
		// Down and to Right
		count = 0;
		for (int j = i; j < 8; j++) {
			count += board[j-i][j];
		}
		if (count > 1) {
			valid = false;
		}

		// Down and to Left
		count = 0;
		for (int j = i; j < 8; j++) {
			count += board[8-1-j][j-i];
		}
		if (count > 1) {
			valid = false;
		}

		// Up and to Right
		count = 0;
		for (int j = i; j < 8; j++) {
			count += board[j][8-1-j+i];
		}
		if (count > 1) {
			valid = false;
		}

		// Up and to Left
		count = 0;
		for (int j = i; j < 8; j++) {
			count += board[j][j-i];
		}
		if (count > 1) {
			valid = false;
		}
	}

	if (valid) {
		cout << "valid\n";
	}
	else {
		cout << "invalid\n";
	}
}