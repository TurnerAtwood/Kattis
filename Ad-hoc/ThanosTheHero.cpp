/*	Turner Atwood
 *	4/9/19
 *	Thanos The Hero [3.5] : (https://open.kattis.com/problems/thanosthehero)
 *	TRIVIAL - Iterate over the list backwards and check each element
 */

#include <iostream>
#include <algorithm>

using namespace std;

// Fastest Input
void fastscan(int &number);

int main() {
	// Trying to make input faster
	ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
	
	// Grab all of the numbers (in reverse)
	int N;
	fastscan(N);
	int Pops[N];
	for (int i = 0; i < N; i++) {
		fastscan(Pops[N-1-i]);
	}

	long killCount = 0;
	int current, previous;
	for (int i = 1; i < N; i++) {
		previous = Pops[i-1];
		current = Pops[i];
		// Not possible to establish a strict ordering
		if (previous == 0) {
			killCount = 1;
			break;
		}
		// Nothing needs to be done here
		if (current < previous) {
			continue;
		}
		Pops[i] = previous-1;
		killCount += (current - Pops[i]);
	}

	cout << killCount << "\n";
}

// Fast integer grabber
void fastscan(int &number) 
{ 
    //variable to indicate sign of input number 
    bool negative = false; 
    register int c; 
  
    number = 0; 
  
    // extract current character from buffer 
    c = getchar(); 
    if (c=='-') 
    { 
        // number is negative 
        negative = true; 
  
        // extract the next character from the buffer 
        c = getchar(); 
    } 
  
    // Keep on extracting characters if they are integers 
    // i.e ASCII Value lies from '0'(48) to '9' (57) 
    for (; (c>47 && c<58); c=getchar()) 
        number = number *10 + c - 48; 
  
    // if scanned input has a negative sign, negate the 
    // value of the input number 
    if (negative) 
        number *= -1; 
} 
