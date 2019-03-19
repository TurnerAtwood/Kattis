/*	Turner Atwood
 *	3/13/19
 *	Troll Hunt
 *	Ad-Hoc 100%
 */

#include <iostream>
#include <cmath>

using namespace std;

int main() {
	// Bridges, Knights, Knights Per Group
	int B,K,G;
	cin >> B >> K >> G;
	cout << ceil((B-1.0)/(K/G)) << endl;;
}