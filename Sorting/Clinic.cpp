/*  Turner Atwood
 *  10/11/20
 *  Clinic [3.1] open.kattis.com/problems/clinic
 *  PriorityQueue/Set - Penalize new arrivals more than old
 */

#include <iostream>
#include <string>
#include <unordered_set>
#include <queue>

using namespace std;

struct tup {
    long time;
    string name;
};

// Sort by time THEN name
bool operator<(const tup& a, const tup& b){
    if (a.time == b.time) {
        return a.name > b.name;
    }
    return a.time < b.time;
}

string smallest_name(unordered_set<string> names) {
    string best = *names.begin();
    for (unordered_set<string>::iterator it = names.begin(); it != names.end(); it++) {
        if (*it < best) {
            best = *it;
        }
    }
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long N,K,Q,T,S;
    string M;

    unordered_set<string> quitters;
    string found;
    priority_queue<tup> pq;

    cin >> N >> K;
    for (int i = 0; i < N; i++) {
        cin >> Q >> T;
        // Push onto the queue
        if (Q == 1) {
            cin >> M >> S;
            pq.push((tup){S - T*K, M});
        }
        // Pop off the queue
        else if (Q == 2) {
            tup patient;
            string found = "";

            while (!pq.empty()) {
                patient = pq.top();
                pq.pop();

                if (quitters.count(patient.name) == 0) {
                    found = patient.name;
                    break;
                }
            }
            
            if (found != "") {
                cout << found << "\n";
            }
            else {
                cout << "doctor takes a break\n";
            }
        }
        // Someone left
        else {
            cin >> M;
            quitters.insert(M);
        }
    }
}
