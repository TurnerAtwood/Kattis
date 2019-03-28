/*	Turner Atwood
 *	3/25/19
 *	Coloring Socks [3.1] : (https://open.kattis.com/problems/color)
 *	Count the socks of each color and create sliding windows to add them to washers
 */

#include <iostream>
#include <map>

using namespace std;

int main() {
	// Input
	map<int,int> numbers;
	int S,C,K;
	cin >> S >> C >> K;
	int num;
	// Add the count of each sock to the map
	for (int i = 0; i < S; i++) {
		cin >> num;
		if (numbers.count(num)) {
			numbers[num]++;
		}
		else {
			numbers[num] = 1;
		}
	}

	// Init variables
	int washers = 0;
	int leftovers = 0;
	int thisColor,count;
	int lastColor = 0;

	// Try socks for every color (least to greatest)
	for (map<int,int>::iterator it = numbers.begin(); it != numbers.end(); it++) {
		thisColor = it->first;
		count = it->second;
		// If the last washer has room
		if (leftovers != 0) {
			// Check to see if these socks can go in it
			if (thisColor - lastColor <= K) {
				count += leftovers;
			}
			// If not, start a new washer
			else {
				washers++;
			}
		}
		// Fill all possible washers 
		washers  += count / C;
		leftovers = count % C;
		lastColor = thisColor;
	}
	// Include any remaining socks in a final washer
	if (leftovers > 0) {
		washers++;
	}

	// Output
	cout << washers << endl;

}