/*	Turner Atwood
 *	3/12/19
 *	Conformity [3.2] : (https://open.kattis.com/problems/conformity)
 *	Sort the schedules and add them to a map, then print the sum of max total
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

string getInput();

int main() {
	int N;
	cin >> N;
	unordered_map<string,int> popularity;
	// Populate the popularity map with the input
	for (int i = 0; i < N; i++) {
		string student = getInput();
		// Update the map with this student's schedule
		if (popularity.count(student) == 0) {
			popularity[student] = 1;
		}
		else {
			popularity[student] = popularity[student] + 1;

		}
	}

	// Find all of the best schedules and print the total
	int count = 0;
	int bestNum = 0;
	for (unordered_map<string,int>::iterator it = popularity.begin(); it != popularity.end(); it++) {
		if (it->second > bestNum) {
			count = 0;
			bestNum = it->second;
		}
		if (it->second == bestNum) {
			count += 1;
		}
	}
	cout << bestNum * count << endl;

}

// Take input and spit out the sorted list as a string
string getInput() {
	string result;
	vector<int> schedule;
	int item;
	for (int j = 0; j < 5; j++) {
		cin >> item;
		schedule.insert(schedule.end(), item);
	}
	sort(schedule.begin(), schedule.end());
	for (int j = 0; j < 5; j++) {
		result += to_string(schedule.at(j));
	}
	return result;
}