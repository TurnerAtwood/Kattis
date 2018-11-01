#include<iostream>

using namespace std;

int main() {
	int X,N,P,total;
	cin >> X;
	cin >> N;
	total = X*(N+1);
	for (int i = 0; i < N; i++) {
		cin >> P;
		total -= P;
	}
	cout << total << endl;
}