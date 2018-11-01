#include<iostream>

using namespace std;

int main() {
	int M,A,B,C;
	cin >> M;
	cin >> A;
	cin >> B;
	cin >> C;
	int avail = 2*M-A-B;
	if (C > avail)
		cout << "impossible" << endl;
	else
		cout << "possible" << endl;
}