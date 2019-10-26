"""
/*  Turner Atwood
 *  9/10/19
 *  Baby Bites [1.7] https://open.kattis.com/problems/babybites
 *  Ad-hoc
 */
"""

def main():
    num = int(input())
    words = input().split(" ")
    fail = False
    for i in range(len(words)):
        word = words[i]
        if word == "mumble":
            continue
        if not word == str(i+1):
            fail = True
            break
    if not fail:
        print("makes sense")
    else:
        print("something is fishy")

if __name__ == "__main__":
    main()