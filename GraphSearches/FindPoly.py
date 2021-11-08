"""
 * Turner Atwood
 * 11/7/2021
 * Find Poly [3.1] (https://open.kattis.com/problems/findpoly)
 * BFS - A unionfind is overkill to find figures - BFS and ensure all
 ** points have exactly two line segments to count a polygon.
 */
"""

from sys import stdin
from collections import deque

def main():
    pt_map = dict()
    for line in stdin:
        line = line.strip()[:-1]
        if not line:
            continue
        for seg in line.split(";"):
            p1, p2 = eval( "(%s)" % seg )
            if p1 not in pt_map:
                pt_map[p1] = set()
            pt_map[p1].add(p2)

            if p2 not in pt_map:
                pt_map[p2] = set()
            pt_map[p2].add(p1)

    visited = set()
    fig_count = 0
    poly_count = 0

    # Try a BFS from every point
    # A BFS is a poly if every node has exactly 2 endpoints until you reach the start
    for start in pt_map:
        if start in visited:
            continue
        fig_count += 1
        poly = True

        bfs_queue = deque( [start] )
        while bfs_queue:
            cur_pt = bfs_queue.popleft()
            if cur_pt in visited:
                continue
            visited.add(cur_pt)
            cur_neighs = pt_map[cur_pt]
            poly &= len(cur_neighs) == 2 # Not a Poly if we ever see a branch
            for neigh_pt in cur_neighs:
                if not neigh_pt in visited:
                    bfs_queue.append(neigh_pt)
        poly_count += poly
    print(fig_count, poly_count)

if __name__ == "__main__":
    main()

