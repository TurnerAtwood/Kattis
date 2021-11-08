"""
/* Turner Atwood
 * 11/6/2021
 * Variable Arithmetic [2.5] (https://open.kattis.com/problems/variablearithmetic)
 * Dictionary : Most direct use-case of a map possible
 */
"""

def main():
    names = dict()
    while True:
        line = input().split()
        total = 0
        out_str = []
        if line == ["0"]:
            break
        if "=" in line:
            names[line[0]] = int(line[2])
            continue
        for item in line[::2]:
            if item in names:
                total += names[item]
                continue
            try:
                total += int(item)
            except ValueError as E:
                out_str.append(item)
        if total:
            out_str = [str(total)] + out_str
        out_line = " + ".join(out_str)
        print(out_line)


if __name__ == "__main__":
    main()

