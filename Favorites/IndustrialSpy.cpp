/*	Turner Atwood
 *	2/23/19
 *	An Industrial Spy [https://open.kattis.com/problems/industrialspy] : (3.3)
 *	Use a prime siev to get all of the primes from 1-10^8
 **	Then generate all of the possible numbers from the given digits
 **	Finally, check to see how many of the possibles are prime
 */

# include <iostream>
# include <vector>
# include <unordered_set>
# include <algorithm>
using namespace std;

static int LIMIT = 10000000;

bool* makeSiev();
vector<int>* makePossible(string);
int countInstances(int, int);

int main() {
	int C;
	cin >> C;
	bool* siev = makeSiev();
	for (int z = 0; z < C; z++) {
		string number;
		cin >> number;
		vector<int>* possible = makePossible(number);

		//cout << "Possible:\n";
		int count = 0;
		for (int i = 0; i < possible->size(); i++) {
			//printf("%d, ", possible->at(i));
			if (siev[possible->at(i)]) {
				count++;
			}
		}
		cout << count << endl;
	}
}

// One of the fastest way to generate all primes in a given range
bool* makeSiev() {
	bool* result = new bool[LIMIT];
	result[0] = false;
	result[1] = false;
	for (int i = 2; i < LIMIT; i++) {
		result[i] = true;
	}
	int i = 1;
	while (i*i < LIMIT) {
		i += 1;
		if (!result[i]) {
			continue;
		}
		for (int j = i*i; j <= LIMIT; j += i) {
			result[j] = false;
		}
	}
	return result;
}

// This is a ton of data structure manipulation - couldn't see how to use next_permutation
// Essentially just build all numbers of length 1,2,...,n, where n is the number of digits given
// Use vectors to store the final & intermediate sets of numbers and a set to prevent duplicates
vector<int>* makePossible(string number) {
	// Initalizeing most of the variables used
	unordered_set<int>* seen = new unordered_set<int>();
	int size = number.size();
	int num = stoi(number);
	vector<int>* result = new vector<int>();
	vector<int>* last_result = new vector<int>();
	int digits[7];
	int dig_freq[] = {0,0,0,0,0,0,0,0,0,0};
	int tmp_num = num;
	// Build the array of digits (also paths of length 1)
	for (int i = 0; i < size; i++) {
		int digit = tmp_num%10;
		if (seen->count(digit) == 0 && digit != 0) {
			result->insert(result->end(), digit);
			last_result->insert(last_result->end(), digit);
		}
		digits[i] = digit;
		seen->insert(digit);
		dig_freq[digit] += 1;
		tmp_num = tmp_num/10;
	}

	// Build the paths of length 2 - n
	for (int i = 1; i < size; i++) {
		
		// This stores all numbers generated of length i
		vector<int>* tmp_result = new vector<int>();

		// Try every number of length i-1 with every digit available
		for (int j = 0; j < last_result->size(); j++) {
			int number = last_result->at(j);
			for (int k = 0; k < size; k++) {
				int digit = digits[k];
				int available = dig_freq[digit];
				int used = countInstances(number, digit);
				int new_number = number*10 + digit;
				// Don't try to use more digits then you have, and do not repeat numbers
				if (used < available && seen->count(new_number) == 0) {
					tmp_result->insert(tmp_result->end(), new_number);
					seen->insert(new_number);
				}
			}
		}

		// Put the paths of length i into the temp vector to use in the next loop
		last_result = new vector<int>();
		last_result->insert(last_result->end(), tmp_result->begin(), tmp_result->end());
		// Store all of the paths of length i generated in the final result
		result->insert(result->end(), tmp_result->begin(), tmp_result->end());
	}

	return result;
}

// Used to count how many times digits appears in the given number
int countInstances(int number, int digit) {
	int count = 0;
	if (digit > 9 || digit < 0) {
		cout << "DON'T DO THAT.";
		return 0;
	}
	while (number > 0) {
		if (number%10 == digit) {
			count++;
		}
		number = number / 10;
	}
	return count;
}