/*	Turner Atwood
 *	10/16/19
 *	Recount [2.2] https://open.kattis.com/problems/recount
 *	Basic Map
 */

#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
	unordered_map<string,int> votes;
	string name;
	getline(cin, name);
	int count = 0;
	int max_name_count = 0;
	string max_name = "";
	int max = 0;
	while (name != "***") {
		if (!votes.count(name)) {
			votes[name] = 0;
		}
		votes[name]++;

		if (votes[name] > max) {
			max = votes[name];
			max_name_count = 1;
			max_name = name;
		}
		else if (votes[name] == max) {
			max_name_count += 1;
		}

		count++;
		getline(cin, name);
	}

	if (max_name_count > 1) {
		cout << "Runoff!\n";
	}
	else {
		cout << max_name << endl;
	}
}