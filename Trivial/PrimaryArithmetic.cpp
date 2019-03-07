/*	Turner Atwood
 *	3/7/19
 *	Primary Arithmetic [2.9] : (https://open.kattis.com/problems/primaryarithmetic)
 *	Compare each digit in a,b to the corresponding digit in (a+b)
 **	If they differ (account for previous carries) then that digit is carried
 */

#include <iostream>

using namespace std;

int main() {
	int a,b;
	cin >> a >> b;
	while (a > 0 || b > 0) {
		int count = 0;
		int carry = 0;
		int sum = a + b;
		while (sum != 0) {
			// Look at the last digit of each number
			int sum_d = sum%10;
			int a_d = a%10;
			int b_d = b%10;
			// Set up the next loop
			sum /= 10;
			a /= 10;
			b /= 10;
			// Carry detection
			if (a_d + b_d + carry != sum_d) {
				carry = 1;
				count++;
			}
			else {
				carry = 0;
			}
		}
		// Output
		if (count == 0) {
			printf("No carry operation.\n");
		}
		else if (count == 1) {
			printf("1 carry operation.\n");
		}
		else {
			printf("%d carry operations.\n", count);
		}
		// Next input
		cin >> a >> b;
	}
}