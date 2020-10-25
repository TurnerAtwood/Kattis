"""
/*  Turner Atwood
 *  10/14/2020
 *  Zig Zag Nametag [3.7] open.kattis.com/problems/zigzag
 *  Ad-hoc: Every 25 needs a letter in a "az" pattern
 ** Overshoot the 25 then move up letters to go down to the target
 */
"""

BASE_VAL = ord("a")

def score(name):
    total = 0
    prev = 0
    for let in name:
        total += abs(let - prev)
        prev = let
    return total

def main():
    n = int(input())

    size = (n-1)//25 + 1
    choices = [25, 0]

    res = [0]
    for i in range(size):
        res.append(choices[i%2])

    cur_score = 25 * (len(res)-1)

    if size == 1:
        res[1] = n
        cur_score = n

    while cur_score > n+1:
        res[1] -= 1
        cur_score -= 2

    if cur_score > n:
        if res[-1] == 0:
            res[-1] = 1
        else:
            res[-1] = 24

    return "".join([chr(BASE_VAL + i) for i in res])

if __name__ == "__main__":
    print(main())
