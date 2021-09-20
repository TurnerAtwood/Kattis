"""
/*  Turner Atwood
 *  9/19/2021
 *  Checking For Correctness [4.2]: (https://open.kattis.com/problems/checkingforcorrectness)
 *  Ad-hoc : Eval for + and *, for ^, compute it quickly using the binary expansion of the exponent
 */
"""

import sys

def exp(a, b):
    tot, exp = 1, a

    for pwr in bin(b)[2:][::-1]:
        # print(f"{pwr}: {exp}")
        if pwr == "1":
            tot = (tot * exp) % 10000
        exp = (exp * exp) % 10000
    return tot

def main():
    out = list()
    for line in sys.stdin:
        n1, op, n2 = line.split()
        n1 = int(n1[-4:])
        if op != "^":
            n2 = int(n2[-4:])
            out.append( str(eval(f"{n1} {op} {n2}")%10000) )
        else:
            n2 = int(n2)
            out.append( str(exp(n1, n2)) )
    out.append("")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

