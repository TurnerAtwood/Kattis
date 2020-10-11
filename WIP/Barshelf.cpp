#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <unordered_set>

#define printf __mingw_printf

using namespace std;

// Helper items
struct tup{
    int index;
    int left;
    int right;
};

void arrPrint(vector<int> arr) {
    for (int i = 0; i < arr.size(); i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}

// BST class for remembering left counts (data comes sorted)
class BST {
    public:
    vector<int> tree;
    vector<int> counts;
    int m;

    // Constructor
    BST(vector<int> source) {
        int n = source.size();
        m = 2*n;
        tree = *(new vector<int>(m, 0));
        counts = *(new vector<int>(m, 0));

        stack<tup> tup_stack;
        tup_stack.push((tup){0, 0, n-1});

        int left,right,index;
        while(!tup_stack.empty()) {
            tup cur_tup = tup_stack.top();
            tup_stack.pop();

            index = cur_tup.index;
            left = cur_tup.left;
            right = cur_tup.right;

            int middle = (left+right)%2 + (left + right) / 2;
            tree[index] = source[middle];

            if (middle+1 <= right)
                tup_stack.push((tup){2*index+2, middle+1, right});
            if (left <= middle-1)
                tup_stack.push((tup){2*index+1, left, middle-1});
        }
    }

    // Get index of the largest element le target 
    int find(int target) {
        int cur_index = 0;
        int best_index = -1;
        int cur_val;


        while (valid_index(cur_index)) {
            cur_val = tree[cur_index];

            if (target < cur_val) {
                cur_index = 2*cur_index + 1;
            }
            else if (target > cur_val) {
                if (best_index == -1 or cur_val > tree[best_index])
                    best_index = cur_index;
                cur_index = 2*cur_index + 2;
            }
            else {
                best_index = cur_index;
                break;
            }
        }
        // printf("[%d]: %d -> %d\n", target, best_index, tree[best_index]);
        return best_index;
    }

    // Get the total count of items le the given value in the bst
    int count(int value) {
        int index = find(value);

        // Searching for something below the lowest element
        if (index == -1)
            return 0;

        int total = 0; 
        bool left_parent = true;
        while(true) {
            if (left_parent)
                total += counts[index];
            
            if (index == 0)
                break;

            left_parent = (index%2 == 0);
            index = (index - 1)/2;
        }
        return total;
    }
    
    // Update the left_child count in the bst for the given value and its parents
    void update_count(int value) {
        int index = find(value);

        bool right_parent = true;
        while(true) {
            if (right_parent)
                counts[index] += 1;

            if (index == 0)
                break;

            right_parent = (index%2 == 1);
            index = (index - 1)/2;
        }
    }

    bool valid_index(int ind) {
         return (ind >= 0 && ind < m && tree[ind] != 0);
    }
    
};

int main() {
    // Input
    int n;
    cin >> n;

    vector<int> bottles(n);
    unordered_set<int> seen_heights;
    for(int i = 0; i < n; i++) {
        cin >> bottles[i];
        seen_heights.insert(bottles[i]);
    }

    // Get a sorted list of the unique bottle heights
    int m = seen_heights.size();
    vector<int> sorted_heights(m);
    copy(seen_heights.begin(), seen_heights.end(), sorted_heights.begin());
    sort(sorted_heights.begin(), sorted_heights.end());

    // Find how many half as smalls are to the right of each bottle
    BST bst(sorted_heights);
    vector<long> half_rights(n,0);
    for (int i = n-1; i >= 0; i--) {
        bst.update_count(bottles[i]);
        half_rights[i] = bst.count(bottles[i]/2);
    }

    // Find how many twice as larges are to the left of each bottle
    // Just negate the data then iterate forwards thru bottles
    reverse(sorted_heights.begin(), sorted_heights.end());
    for (int i = 0; i < m; i++) {
        sorted_heights[i] = -1 * sorted_heights[i];
    }

    bst = *(new BST(sorted_heights));
    vector<long> double_lefts(n,0);
    for (int i = 0; i < n; i++) {
        int bottle = -1 * bottles[i];
        bst.update_count(bottle);


        bottle = bottle*2;
        double_lefts[i] = bst.count(bottle);
    }


    // Count up the middles
    long total = 0;
    for (int i = 0; i < n; i++) {
        total += half_rights[i] * double_lefts[i];
        printf("(%d) %ld\n", i, total);
        if (total < 0) {
            break;
        }
    }

    printf("%ld\n", total);
}

