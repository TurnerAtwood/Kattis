/*	Turner Atwood
 *	10/13/18
 *	CD [4.2] (https://open.kattis.com/problems/cd)
 *	Java and Python would be too slow
 */

#include<iostream>
#include<unordered_set>
using namespace std;


int main() {
	while(true) {
		int num1;
		int num2;
		cin >> num1;
		cin >> num2;
		if (num1 == 0 && num2 == 0) {
			break;
		}

		unordered_set<int> jack = unordered_set<int>();

		for (int i = 0; i < num1; i++) {
			int new_cd;
			cin >> new_cd;
			jack.insert(new_cd);
		}

		int count;
		count = 0;
		for (int i = 0; i < num1; i++) {
			int new_cd;
			cin >> new_cd;
			if (jack.count(new_cd) == 1) {
				count++;
			}
		} 
		cout << count;
		cout << "\n";
	}
}