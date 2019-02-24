/*	Turner Atwood
 *	2/24/19
 *	Arithmetic [4.0] : (https://open.kattis.com/problems/arithmetic)
 *	Base conversion using strings (one line in python)
 **	Ad-hoc math
 */

#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int>* oct_to_bin(string octal);
string bin_to_hex(vector<int>* bin);

int main() {
	string octal;
	cin >> octal;
	vector<int>* bin = oct_to_bin(octal);
	string hex = bin_to_hex(bin);
	cout << hex << endl;
}

// Return the binary of an octal string in a vector
vector<int>* oct_to_bin(string octal) {
	
	vector<int>* bin = new vector<int>();
	// Make sure the vector size will be a multiple of 4
	for (int i = 0; i < octal.size()%4; i++) {
		bin->insert(bin->end(), 0);
	}

	for (int i = 0; i < octal.size(); i++) {
		int digit = octal[i] - '0';
		for (int j = 0; j < 3; j++) {
			bin->insert(bin->end()-j, digit%2);
			digit /= 2;
		}

	}
	return bin;
}

// binary vector (length%4 == 0) to hex string
string bin_to_hex(vector<int>* bin) {
	string hex;
	hex.reserve(bin->size()/4+1);

	for (int i = 0; i < bin->size()/4; i++) {
		// Get the value of the next 4 bin digits
		int digit = 0;
		for (int j = 0; j < 4; j++) {
			digit += bin->at(4*i+j) * pow(2, 3-j);
		}

		// Convert the value from decimal int to hex string
		if (digit < 10) {
			hex += to_string(digit);
		}
		// These would be numbers a-f
		else {
			hex += ('A'+digit-10);
		}
	}

	// Erase all leading zeros
	while (hex[0] == '0') {
		hex = hex.substr(1, hex.size());
	}
	if (hex == "") {
		hex = "0";
	}
	return hex;
}


