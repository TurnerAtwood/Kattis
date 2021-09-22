/*  Turner Atwood
 *  9/20/2021
 *  Baloni [4.2]: (https://open.kattis.com/problems/baloni)
 *  Ad-hoc - Just shoot new arrows as balloons come in, keeping track of past arrows
 */

#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    int heights[1000001] = {0};
    int total = 0;
    int cur_height;
    for (int i = 0; i < N; i++) {
        cin >> cur_height;
        if (heights[cur_height] > 0)
            heights[cur_height]--;
        else
            total++;
        heights[cur_height-1]++;
    }
    printf("%d\n", total);
}
