"""
/* Turner Atwood
 * 11/6/2021
 * Treasure Hunt [2.6] (https://open.kattis.com/problems/treasurehunt)
 * Ad-hoc : Just follow the path given on a 2D list
 */
"""
MOVES = {"N": (-1, 0), "S": (1,0), "W": (0,-1), "E": (0,1)}

def main():
    R,C = [int(i) for i in input().split()]
    arena = [input() for i in range(R)]
    count = 0

    visited = set()
    cur_pos = (0,0)
    while pos_valid(cur_pos, R, C):
        if cur_pos in visited:
            return "Lost"
        visited.add(cur_pos)
        cur_arena = arena[cur_pos[0]][cur_pos[1]]
        if cur_arena == "T":
            return str(count)
        cur_pos = move(cur_pos, cur_arena)
        count += 1

    return "Out"


def move(pos, move):
    return (pos[0] + MOVES[move][0], pos[1] + MOVES[move][1])

def pos_valid(pos, R, C):
    r,c = pos
    return r >= 0 and c >= 0 and r < R and c < C    

if __name__ == "__main__":
    print( main() )

