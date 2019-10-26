/*	Turner Atwood
 *	8/27/19
 *	Shiritori [3.2] https://open.kattis.com/problems/shiritori
 *	Set used to keep track of previous words
 */

#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
	int n;
	cin >> n;
	string thisWord;
	
	// Handle the first word
	cin >> thisWord;
	unordered_set<string> words;
	words.insert(thisWord);
	string lastWord = thisWord;

	int cheater = 0;
	for (int i = 1; i < n; i++) {
		cin >> thisWord;
		if (thisWord.at(0) != lastWord.back() || words.count(thisWord)) {
			cheater = i%2 + 1;
			break;
		}
		
		words.insert(thisWord);
		lastWord = thisWord;
	}

	if (!cheater) {
		printf("Fair Game\n");
	}
	else {
		printf("Player %d lost\n", cheater);
	}
}