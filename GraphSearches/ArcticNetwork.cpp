/*  Turner Atwood
 *  7/6/2021
 *  Arctic Network [4.2]: (https://open.kattis.com/problems/arcticnetwork)
 *  Make a MST (Min. Spanning Tree) then remove the longest S-1 edges (using satellites)
 */

#include <unordered_set>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <set>
#include <map>

using namespace std;

double arctic_network(void);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        printf("%.02lf\n", arctic_network());
    }
}

double arctic_network(void) {
    int S,P,i;
    cin >> S >> P;
    S--;

    // Save the coordinates for distance calculations
    int cds[P][2];
    for (i = 0; i < P; i++)
        cin >> cds[i][0] >> cds[i][1];

    // For the MST gen: Distance -> (target, source)
    multimap<double, pair<int,int>> mst_queue;
    mst_queue.insert( make_pair(0, make_pair(0,0)) );
    
    multiset<double> mst_edges;
    unordered_set<int> visited;
    multimap<double, pair<int,int>>::iterator q_it;
    int cur_ind;
    double dist;

    // Generate a MST of the given vertices
    while (mst_queue.size() != 0) {
        q_it = mst_queue.begin();
        mst_queue.erase(q_it);

        cur_ind  = (*q_it).second.first;
        if (visited.count(cur_ind) != 0)
            continue;

        visited.insert(cur_ind);
        if (cur_ind != 0)
            mst_edges.insert( (*q_it).first );

        for (i = 0; i < P; i++) {
            if (visited.count(i) != 0) continue;
            dist = (cds[i][0]-cds[cur_ind][0])*(cds[i][0]-cds[cur_ind][0]) + (cds[i][1]-cds[cur_ind][1])*(cds[i][1]-cds[cur_ind][1]);
            mst_queue.insert( make_pair(dist, make_pair(i, cur_ind)) );
        }
    }

    // Remove the longest S-1 vertices by attaching a satellite to their local networks
    for (i = 0; i < S; i++)
        mst_edges.erase(--mst_edges.end());
    return sqrt( (*--mst_edges.end()) );
}

