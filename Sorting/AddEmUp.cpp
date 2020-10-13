/*  Turner Atwood
 *  10/12/20
 *  Add Em Up [4.2] open.kattis.com/problems/addemup
 *  Throw all the numbers and their flips into a map
 ** Put at most 2 of each item into a list, sort, then linear scan
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

static int flip_digit[] = {0,1,2,-1,-1,5,9,-1,8,6};

long flip(long num) {
    long result = 0;
    while (num) {
        int digit = num%10;
        digit = flip_digit[digit];
        if (digit == -1)
            return -1;
        result = result*10 + digit;
        num /= 10;
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long N,S;
    cin >> N >> S;

    // Add each number and its flipped form (if valid/possible)
    unordered_map<long,int> nums;
    long num,flipped;
    for (int i = 0; i < N; i++) {
        cin >> num;
        if (nums.count(num) == 0)
            nums[num] = 0;
        nums[num] += 1;

        flipped = flip(num);
        if (flipped != num) {
            if (nums.count(flipped) == 0)
                nums[flipped] = 0;
            nums[flipped] += 1;
        }
    }
    nums.erase(-1);

    // Insert up to 2 of each number from all of the numbers we saw above. Then sort
    vector<long> sorted_nums;
    for (unordered_map<long,int>::iterator it = nums.begin(); it != nums.end(); it++) {
        sorted_nums.push_back(it->first);
        if (it->second > 1)
            sorted_nums.push_back(it->first);
    }
    sort(sorted_nums.begin(), sorted_nums.end());

    // Start at each end and try to hone in on the target
    int left = 0;
    int right = sorted_nums.size()-1;
    long l_val,r_val,total;
    while (left < right) {
        l_val = sorted_nums[left];
        r_val = sorted_nums[right];
        total = l_val + r_val;

        if (total < S) {
            left++;
        }
        else if (total > S) {
            right--;
        }
        else {
            // Ensure you aren't using the same card flipped
            if (l_val != flip(r_val) || nums[l_val] > 1) { 
                cout << "YES\n";
                return 0;
            }
            right--;
        }
    }
    cout << "NO\n";
}

