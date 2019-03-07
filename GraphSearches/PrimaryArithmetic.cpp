/*	Turner Atwood
 *
 *
 *
 */

#include <iostream>

using namespace std;

int main() {
	int a,b;
	cin >> a >> b;
	while (a != 0 && b != 0) {
		int count = 0;
		while (a != 0 && b != 0) {
			int dig_a = a%10;
			int dig_b = b%10;
			if (dig_a + dig_b > 9) {
				count++;
			}
			a /= 10;
			b /= 10;
		}
		cout << count;
		cin >> a >> b;
	}
}