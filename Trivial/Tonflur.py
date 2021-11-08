"""
/* Turner Atwood
 * 11/6/2021
 * Tonflur [2.6] (https://open.kattis.com/problems/toflur)
 * Trivial - Taking items in sorted order is optimal
 */
"""

def main():
    n = int(input())
    tiles = sorted([int(i) for i in input().split()])
    score = 0
    for i in range(n-1):
        score += (tiles[i] - tiles[i+1]) * (tiles[i] - tiles[i+1])
    print(score)


if __name__ == "__main__":
    main()

