/*	Turner Atwood
 *	2/26/19
 *	Secret Message [1.9] : (https://open.kattis.com/problems/secretmessage)
 *	Trivial 2D array manipulation
 */

#include <iostream>

using namespace std;

int matrixSize(int N);

int main() {
	int N;
	cin >> N;
	for (int z = 0; z < N; z++) {
		string line;
		cin >> line;
		int size = matrixSize(line.size());
		char table[size][size];
		// ROTATE as the table is built (notice indeces)
		for (int i = 0; i < line.size(); i++) {
			table[i%size][size-i/size-1] = line[i];
		}
		for (int i = line.size(); i < size*size; i++) {
			table[i%size][size-i/size-1] = '0';
		}

		// Print out the table (ignore placeholder 0's)
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < size; j++) {
				if (table[i][j] != '0')
					cout << table[i][j];
			}
		}
		cout << endl;
	}
}

// return the smallest square less than or equal to N
int matrixSize(int N) {
	int i = 0;
	while (i*i < N) {
		i += 1;
	}
	return i;
}