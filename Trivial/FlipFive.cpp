/*  Turner Atwood
 *  7/6/2021
 *  Flip Five [3.0] : (https://open.kattis.com/problems/flipfive)
 *  Brute-force - Try all Paths in a BFS.
 */

#include <iostream>
#include <stdio.h>
#include <unordered_set>
#include <unordered_map>
#include <list>

using namespace std;

unordered_map<int,int> all_boards(void);
int board_move(int,int);

int main() {
    int P, board;
    char item;
    int base;
    cin >> P;

    unordered_map<int,int> distances = all_boards();

    for (int i = 0; i < P; i++) {
        // Read in new board
        base = 1;
        board = 0;
        for (int j = 0; j < 9; j++) {
            cin >> item;
            if (item == '*')
                board += base;
            base *= 10;
        }

        // Just grab the calculated distance and print it
        printf("%d\n", distances[board]);
    }
}

// Generate all possible boards and how far they are from board 000000000
unordered_map<int,int> all_boards(void) {
    int board = 0;
    int depth = 0;
    int board_new;

    unordered_map<int,int> distances;
    list<int> path_queue;
    path_queue.push_back(board);
    distances[board] = depth;

    while (path_queue.size() != 0) {
        board = path_queue.front();
        depth = distances[board];
        path_queue.pop_front();

        for (int i = 0; i < 9; i++) {
            board_new = board_move(board, i);
            if (distances.count(board_new) != 0)
                continue;
            distances[board_new] = depth + 1;
            path_queue.push_back(board_new);
        }
    }

    return distances;
}

// Unpack board into array, make a move, return re-packed board
int board_move(int board_old, int move) {
    int board_new[9];
    for (int i = 0; i < 9; i++) {
        board_new[8-i] = board_old%10;
        board_old /= 10;
    }

    int packed_board = 0;
    int base = 1;
    for (int i = 0; i < 9; i++) {
        if (i == move || i == move+3 || i == move-3 || (i == move+1 && i/3 == (move)/3) || (i == move-1 && i/3 == (move)/3))
            board_new[i] = ! board_new[i];
        packed_board += board_new[i] * base;
        base *= 10;
    }
    return packed_board;
}

