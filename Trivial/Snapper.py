"""
/* Turner Atwood
 * 11/6/2021
 * Snapper Chain (Easy) [2.6] (https://open.kattis.com/problems/snappereasy)
 * A chain of n snappers turns on the light if k%(2^n) == (2^n)-1
 */
"""
MOVES = {"N": (-1, 0), "S": (1,0), "W": (0,-1), "E": (0,1)}

def main():
    N,K = [int(i) for i in input().split()]
    top = 2**N
    return "ON" if K%top == top-1 else "OFF"

if __name__ == "__main__":
    T = int(input())
    for i in range(1,T+1):
        print("Case #%d: %s" % (i, main()))

