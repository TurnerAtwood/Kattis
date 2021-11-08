"""
/*  Turner Atwood
 *  11/4/2021
 *  Pairing Socks [2.5] (https://open.kattis.com/problems/pairingsocks)
 */ Ad-hoc / Greedy: Use two stacks (Or just a linked list...)
"""

def main():
    n = int(input())
    right = [int(i) for i in input().split()[::-1]]
    left = []
    count = 0

    while right:
        if not left:
            left.append(right.pop())
            count += 1

        if left[~0] == right[~0]:
            left.pop()
            right.pop()
        else:
            left.append(right.pop())
        count += 1

    return str(count) if not left else "impossible"

if __name__ == "__main__":
    print( main() )

