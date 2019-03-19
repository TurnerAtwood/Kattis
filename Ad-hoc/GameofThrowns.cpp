/*	Turner Atwood
 *	3/18/19
 *	Game of Throwns [3.0] : (https://open.kattis.com/problems/throwns)
 *	Ad-hoc - Use a stack to keep track of previous throws
 */

#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	// Initilize input and stack data
	int S,N;
	cin >> S >> N;
	string input;
	int num;
	int current;
	stack<int> order;

	// Start at spot 0 and follow all commands
	order.push(0);
	for (int z = 0; z < N; z++) {
		cin >> input;
		// Put the next spot on the stack
		if (input != "undo") {
			num = stoi(input);
			current = order.top();
			// Make sure the spot is in the range {0,1,...,N-1}
			int next = (current+num)%S;
			if (next < 0) {
				next = S + next;
			}
			order.push(next);
		}
		// Undo a given number of spots
		else {
			cin >> num;
			for (int i = 0; i < num; i++) {
				order.pop();
			}
		}
	}
	// Output the last student on the stack
	cout << order.top() << endl;
}