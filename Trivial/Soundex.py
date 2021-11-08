"""
/*  Turner Atwood
 *  9/23/2021
 *  Soundex Walkway [2.6] : (https://open.kattis.com/problems/soundex)
 *  Sorting
 */ Ad-hoc : Store the coding in a map then linear scan over letters
 """
from sys import stdin

CODE = {"B":1, "F":1, "P":1, "V":1, "C":2, "G":2, "J":2, "K":2, "Q":2, "S":2, "X":2, "Z":2, "D":3, "T":3, "L":4, "M":5, "N":5, "R":6}

def main():
    for line in stdin:
        line = line.strip()
        last_code = None
        out_line = []

        for item in line:
            if item not in CODE:
                last_code = None
                continue
            cur_code = CODE[item]
            if cur_code != last_code:
                out_line.append(str(cur_code))
                last_code = cur_code
        if out_line:
            print("".join(out_line))


if __name__ == "__main__":
    main()
