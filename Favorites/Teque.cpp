/*	Turner Atwood
 *	11/1/19
 *	Teque [3.6] https://open.kattis.com/problems/teque
 *	Keep a list of deques (max size CAP). After the last one
 **	fills, add another to the list and continue. This way, any
 **	index can be efficiently pushed. Dynamic resizing could
 **	make this even more efficient for larger inputs.
 */

int CAP = 10000;

#include <iostream>
#include <deque>
#include <vector>

using namespace  std;

void dump(vector<deque<int>> dqs) {
	for (int i = 0; i < dqs.size(); i++) {
		for (deque<int>::iterator it = dqs[i].begin(); it != dqs[i].end(); it++) {
			cout << *it << " ";
		}
		cout << "| ";
	}
	cout << "\n";
}

int get(vector<deque<int>> &dqs, int index) {
	return (dqs[index/CAP])[index%CAP];
}

// Every deque is kept full (size = CAP) except the last one
void insert(vector<deque<int>> &dqs, int index, int value) {
	int current_dq = index/CAP;
	
	// Add in a new deque if we are appending to the end of a full one
	if (current_dq == dqs.size()) {
		dqs.push_back(deque<int>());
	}

	// Insert the new element
	deque<int>::iterator it = (dqs[current_dq]).begin() + index%CAP;	
	(dqs[current_dq]).insert(it, value);

	// Propogate any overflow down the chain to the end
	while(dqs[current_dq].size() > CAP) {
		int overflow = (dqs[current_dq]).back();
		dqs[current_dq].pop_back();
		
		// Check to see if a new dq needs to be added
		if (current_dq == dqs.size()-1) {
			dqs.push_back(deque<int>());
		}
		current_dq++;
		dqs[current_dq].push_front(overflow);
	}
}

int main() {
	ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 

	int N;
	cin >> N;
	int size = 0;

	vector<deque<int>> dqs;
	string cmd;
	int val,index;

	dqs.push_back(deque<int>());
	for (int i = 0; i < N; i++) {
		cin >> cmd >> val;

		if (cmd == "get") {
			cout << get(dqs, val) << "\n";
			continue;
		}

		if (cmd == "push_front") {
			index  = 0;
		}
		else if (cmd == "push_middle") {
			index = (size+1)/2;
		}
		else {
			index = size;
		}
		
		insert(dqs, index, val);
		size++;
	}
}