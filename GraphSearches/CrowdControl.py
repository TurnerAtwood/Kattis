"""
/*  Turner Atwood
 *  10/25/2020
 *  Crowd Control [3.2] open.kattis.com/problems/crowdcontrol
 *  Dijkstra's SSSP to find the path. Then print all unused streets
 ** off of intersections along the path.
 */
"""

import heapq
from sys import stdin
from math import inf

def main():
    N,M = [int(i) for i in stdin.readline().split()]

    neighs = [dict() for i in range(N)]
    st_inds = dict()

    for i in range(M):
        a,b,c = [int(i) for i in stdin.readline().split()]
        neighs[a][b] = -1*c
        neighs[b][a] = -1*c
        st_inds[(a,b)] = i
        st_inds[(b,a)] = i

    path = dijkstra(neighs)

    used_sts = {st_inds[(path[i], path[i+1])] for i in range(len(path)-1)}
    seen_sts = set()
    for c_ind in path:
        for n_ind in neighs[c_ind]:
            seen_sts.add(st_inds[(c_ind, n_ind)])

    block_sts = sorted(seen_sts - used_sts)
    if block_sts:
        print(" ".join([str(st) for st in block_sts]))
    else:
        print("none")


# Return the path from 0 to N-1
def dijkstra(neighs):
    costs = dict()
    sources = dict()
    N = len(neighs)

    pq = [ (-1*inf, 0, -1) ]
    while pq:
        c_cost,c_ind,c_src = heapq.heappop(pq)

        if c_ind in costs:
            continue
        costs[c_ind] = c_cost
        sources[c_ind] = c_src

        # Guaranteed a path exists
        if c_ind == N-1:
            break

        for n_ind in neighs[c_ind]:
            if n_ind in costs:
                continue

            n_cost = max(c_cost, neighs[c_ind][n_ind])
            heapq.heappush(pq, (n_cost, n_ind, c_ind) )

    path = list()
    ind = N-1
    while ind != -1:
        path.append(ind)
        ind = sources[ind]

    return path


if __name__ == "__main__":
    main()

