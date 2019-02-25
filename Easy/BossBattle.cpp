/*	Turner Atwood
 *	2/24/19
 *	Boss Battle [1.8] : (https://open.kattis.com/problems/bossbattle)
 *	Trivial
 */

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	cout << max(1,N-2) << endl;
}