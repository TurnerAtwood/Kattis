/*  Turner Atwood
 *  10/15/2020
 *  Intelligence Infection [6.3] open.kattis.com/problems/intelligenceinfection
 *  Graph - Use a directed graph storing spies parents and children.
 ** Isolate enemies and friends who lead to enemies. Find all top-level
 ** spies and cycles without a trunk leading in.
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Store each spy's parents & children and who is an enemy

    int S,E,C;
    cin >> S >> E >> C;

    vector<unordered_set<int>> parents(S);
    vector<unordered_set<int>> children(S);
    
    int spy1, spy2;
    for (int i = 0; i < C; i++) {
        cin >> spy1 >> spy2;
        children[spy1].insert(spy2);
        parents[spy2].insert(spy1);
    }

    unordered_set<int> tainted;
    unordered_set<int> enemies;
    for (int i = 0; i < E; i++) {
        cin >> spy1;
        tainted.insert(spy1);
        enemies.insert(spy1);
    }

    // Remove the parents and children of every spy who
    // leads to an enemy because they won't get a public message
    vector<int> stack(tainted.size());
    copy(tainted.begin(), tainted.end(), stack.begin());

    while (!stack.empty()) {
        int taint = stack.back();
        stack.pop_back();

        // All parents of a tainted node are tainted
        unordered_set<int> p = parents[taint];
        for (unordered_set<int>::iterator it = p.begin(); it != p.end(); it++) {
            if (tainted.count(*it) == 0) {
                tainted.insert(*it);
                stack.push_back(*it);
            }
            children[*it].erase(taint);
        }

        // Remove the links to the children of tainted ones
        unordered_set<int> c = children[taint];
        for (unordered_set<int>::iterator it = c.begin(); it != c.end(); it++) {
            parents[*it].erase(taint);
        }
    
        parents[taint].clear();
        children[taint].clear();
    }

    unordered_set<int> uncovered;
    for (int i = 0; i < S; i++) {
        uncovered.insert(i);
    }
    unordered_set<int> trunks;

    // Spies without parents are trunks, they will get public messages
    // Mark everyone who would recieve their public msg as covered
    for (int i = 0; i < S; i++) {
        if (parents[i].size() != 0)
            continue;

        trunks.insert(i);

        if (enemies.count(i) != 0) {
            uncovered.erase(i);
            continue;
        }

        stack.push_back(i);
        while (!stack.empty()) {
            int top = stack.back();
            stack.pop_back();

            if (uncovered.count(top) == 0)
                continue;
            uncovered.erase(top);
                
            unordered_set<int> c = children[top];
            for (unordered_set<int>::iterator it = c.begin(); it != c.end(); it++) {
                stack.push_back(*it);
            }
        }
    }
    
    // Everything still uncovered is in a cycle w/o a trunk feeding in
    // So, pick any element to cover the cycle and cover it
    while (!uncovered.size() == 0) {
        int trunk = *uncovered.begin();
        trunks.insert(trunk);

        stack.push_back(trunk);
        while (!stack.empty()) {
            int top = stack.back();
            stack.pop_back();

            if (uncovered.count(top) == 0)
                continue;
            uncovered.erase(top);

            unordered_set<int> c = children[top];
            for (unordered_set<int>::iterator it = c.begin(); it != c.end(); it++) {
                stack.push_back(*it);
            }
        }
    }

    // Give every "trunk" a message except enemies
    cout << trunks.size() - E << "\n";
}

