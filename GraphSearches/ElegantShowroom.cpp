/*  Turner Atwood
 *  10/24/2020
 *  Elegant Showroom [4.3] open.kattis.com/problems/showroom
 *  Dijkstra's SSSP over a grid. Doors cost zeros, cars cost 1
 */

#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <vector>

using namespace std;

// Items needed to support a priority_queue
struct tup{
    int cost;
    int index;
};

bool operator < (const tup& a, const tup& b) {
    return a.cost > b.cost;
}

// Row-major indexing neighbor grabber
// Never include walls in neighbor lists)
vector<int> get_neighs(int* grid, int R, int C, int target) {
    int dirs[4] = {-1*C, 1, C, -1};
    vector<int> result;

    for (int i = 0; i < 4; i++) {
        int dir = dirs[i];
        int ind = target + dir;

        if (ind < 0 || ind >= R*C)          // In-bounds
            continue;
        if (i%2 == 1 && ind/C != target/C)  // left/right stay on same row
            continue;
        if (grid[ind] == 2)
            continue;
        result.push_back(ind);
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Grab the grid
    int R,C;
    cin >> R >> C;
    int size = R*C;
    
    unordered_map<int,int> neighs[size];
    int grid[size];
    char val;
    for (int i = 0; i < size; i++) {
         cin >> val;
         if (val == 'c')
             grid[i] = 1;
         else if (val == 'D')
             grid[i] = 0;
        else
            grid[i] = 2;
    }

    // Grab target
    int t_r,t_c;
    cin >> t_r >> t_c;
    int target = (t_r-1)*C + (t_c-1);
    
    // Build neighbors (ignore walls)
    vector<int> cur_neighs;
    for (int i = 0; i < size; i++) {
        if (grid[i] == 2)
            continue;
        cur_neighs = get_neighs(grid, R, C, i);
        for (vector<int>::iterator it = cur_neighs.begin(); it != cur_neighs.end(); it++) {
            if (grid[*it] == 'c')
                (neighs[i])[*it] = 1;
            if (grid[*it] == 'D')
                (neighs[i])[*it] = 0;
        }
    }

    priority_queue<tup> pq;
    unordered_map<int,int> costs;

    // Start from exits on the top/bottom rows
    for (int i = 0; i < C; i++) {
        if (grid[i] == 0)
            pq.push((tup){0,i});
        if (grid[size-i-1] == 0)
            pq.push((tup){0, size-i-1});
    }
    
    // Also start from left/right column exits
    for (int i = 1; i < R-1; i++) {
        if (grid[C*i] == 0)
            pq.push((tup){0, C*i});
        if (grid[C*(i+1)-1] == 0)
            pq.push((tup){0, C*(i+1)-1});
    }

    // Dijkstra's to find shorted past to the target
    while (!pq.empty()) {
        tup cur = pq.top();
        pq.pop();

        if (costs.count(cur.index) != 0)
            continue;
        costs[cur.index] = cur.cost; 

        if (cur.index == target)
            break;

        cur_neighs = get_neighs(grid, R, C, cur.index);
        for (vector<int>::iterator it = cur_neighs.begin(); it != cur_neighs.end(); it++) {
            if (costs.count(*it) != 0)
                continue;
            pq.push((tup){cur.cost + grid[*it], *it});
        }
    }
    
    // Output
    cout << costs[target] << "\n";
}

