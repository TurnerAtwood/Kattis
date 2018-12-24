/*	Turner Atwood
	12/24/18
	R2 [1.2] (https://open.kattis.com/problems/r2)
	Trivial Average Calculation
*/

#include <iostream>
using namespace std;

int main() {
	int R1;
	int R2;
	int S;

	cin >> R1;
	cin >> S;
	R2 = 2*S-R1;
	
	printf("%d\n",R2);
	return 0;
}