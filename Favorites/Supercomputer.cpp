/*	Turner Atwood
 *	10/26/19
 *	Supercomputer [4.3] https://open.kattis.com/problems/supercomputer
 *	Use a binary tree. Each node stores the sum of
 **	its children, all the way down to the individual bits.
 **	This gives O(log(n)) lookup and edits!
 */

#include <iostream>
#include <vector>
#include <deque>

using namespace std;

void update(int B, int* tree, int index) {
	int val = tree[B+index];
	val = (val+1)%2;
	tree[B+index] = val;

	if (!val) {
		val = -1;
	}

	index += B;
	while (index > 0) {
		index /= 2;
		tree[index] += val;
	}
}

int rightOf(int B, int* tree, int index) {
	if (index == B) {
		return 0;
	}

	// Binary
	deque<int> dq;
	index += B;
	while (index != 0) {
		dq.push_front(index%2);
		index /= 2;
	}
	dq.pop_front();

	int cur = 1;
	int total = tree[1];
	int dir;
	while (!dq.empty()) {
		dir = dq.front();
		dq.pop_front();
		// GO TO THE RIGHT
		if (dir) {
			total -= tree[2*cur];
		}
		cur = 2*cur+dir;
	}
	return total;
}

int main() {
	int N,K;
	cin >> N >> K;
	int B = 1;
	while (B < N) {
		B *= 2;
	}

	int tree[2*B];
	for (int i = 0; i <= 2*B; i++) {
		tree[i] = 0;
	}

	char type;
	int a,b;
	for (int i = 0; i < K; i++) {
		cin >> type;
		cin >> a;
		a--;
		
		// Update
		if (type == 'F') {
			update(B,tree,a);
			continue;
		}

		// Query
		cin >> b;
		cout << rightOf(B,tree,a) - rightOf(B,tree,b) << "\n";
	}
}