"""
/*  Turner Atwood
 *  10/12/20
 *  A1 Paper [3.8] open.kattis.com/problems/a1paper
 *  Greedy - take tape as needed, starting with the largest papers
 */
"""

def main():
    dims = [2**(-3/4), 2**(-5/4)]
    # Input
    n = int(input())
    papers = [int(i) for i in input().split()]

    cost = 0
    needed = 2
    for i in range(n-1):
        cost = cost + (dims[i%2] * needed/2)
        dims[i%2] /= 2 # Cut the long side in half
        needed = 2 * (needed - min(papers[i], needed))
        if not needed:
            return cost
    return "impossible"

if __name__ == "__main__":
    print(main())

