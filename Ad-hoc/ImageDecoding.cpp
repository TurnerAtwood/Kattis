/*	Turner Atwood
 *	3/27/19
 *	Image Decoding [3.1] : (https://open.kattis.com/problems/imagedecoding)
 *	Ad-hoc - All output formatting
 */

#include <iostream>
#include <set>
#include <sstream>

using namespace std;

int main() {
	// line for input, result contains output
	string line;
	string result;
	
	// Length of the first image
	int N;
	getline(cin, line);
	N = stoi(line);
	while (N != 0) {
		// Starting a new image
		set<int> lengths;
		for (int i = 0; i < N; i++) {
			// Get the pixel from the line
			getline(cin, line);
			istringstream stringLine(line);
			char chr;
			stringLine >> chr;
			int num;
			int length = 0;
			
			// Form the alternating pixel strings
			while (stringLine >> num) {
				length += num;
				for (int j = 0; j < num; j++) {
					result += string(1,chr);
				}

				// Alternate the pixel
				if (chr == '#') {
					chr = '.';
				}
				else {
					chr = '#';
				}		
			}
			// End of individual line
			lengths.insert(length);
			result += "\n";
		}
		// Get the length of the next image
		getline(cin, line);
		N = stoi(line);

		//Add an error line if found
		if (lengths.size() > 1) {
			result += "Error decoding image\n";
		}
		// Append a newline to separate from the next image
		if (N != 0){
			result += "\n";
		}
	}
	// Output the result
	cout << result;
}