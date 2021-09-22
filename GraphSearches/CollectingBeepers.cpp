/*  Turner Atwood
 *  9/20/2021
 *  Collecting Beepers [4.2] : (https://open.kattis.com/problems/beepers)
 *  Travelling Salesman - up to 10 items so not a problem
 */

#include <iostream>
#include <unordered_set>

using namespace std;

void permutations(string str, int i, int n);

int lowest;
int dists[10][10];

// Take in input, compute all distances, then run the salesman
int scenario() {
    int x,y,x0,y0,b;
    cin >> x >> y >> x0 >> y0 >> b;
    int beeps[b][2];
    string ps;
    for (int i = 0; i < b; i++) {
        cin >> beeps[i][0] >> beeps[i][1];
        ps += 'A'+i;
    }

    for (int i = 0; i < b; i++) {
        dists[i][i] = abs(beeps[i][0] - x0) + abs(beeps[i][1] - y0);
        for (int j = i+1; j < b; j++) {
            dists[i][j] = abs(beeps[i][0] - beeps[j][0]) + abs(beeps[i][1] - beeps[j][1]);
            dists[j][i] = dists[i][j];
        }
    }

    lowest = 1000000;
    permutations(ps, 0, b);
    return lowest;
}

// Try every permutation, just use strings to keep track of indices
void permutations(string str, int i, int n)
{
    if (i == n - 1) {
        int tot = dists[str[0]-'A'][str[0]-'A'];
        for (int i = 0; i < n-1; i++) {
            tot += dists[str[i]-'A'][str[i+1]-'A'];
        }
        tot += dists[str[n-1]-'A'][str[n-1]-'A'];
        lowest = min(lowest, tot);
        return;
    }
    for (int j = i; j < n; j++) {
        swap(str[i], str[j]);
        permutations(str, i + 1, n);
        swap(str[i], str[j]);
    }
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        printf("%d\n", scenario());
}

