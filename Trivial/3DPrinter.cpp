/*	Turner Atwood
 *	2/24/19
 *	3D Printer [1.9] : (https://open.kattis.com/problems/3dprinter)
 *	Ad-hoc
 */

#include <iostream>
#include <cmath>

using namespace std;

// Try one more day of printing printers until you do worse than you did the day before
int main() {
	int N;
	cin >> N;
	
	int i = 0;
	int thisDay = N;
	int lastDay = 20000;
	
	while (thisDay <= lastDay) {
		lastDay = thisDay;
		// min. days to print statues + days spent printing printers
		thisDay = ceil(1.0*N/pow(2,i)) + i;
		i++;
	}
	cout << lastDay << endl;
}