"""
/*  Turner Atwood
 *  9/5/2021
 *  Calculator [3.5] : (https://open.kattis.com/problems/calculator)
 *  Just use eval in Python
 */
"""

def main():
    while (True):
        try:
            line = input()
        except:
            break
        out = eval(line)
        print("%.2f" % out)

if __name__ == "__main__":
    main()

