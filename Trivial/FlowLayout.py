"""
/*  Turner Atwood
 *  10/13/20
 *  Flow Layout [2.0] open.kattis.com/problems/flowlayout
 *  Trivial Ad-hoc
 */
"""

def main():
    out = list()
    while True:
        m = int(input())
        if not m:
            break

        boxes = list()
        while True:
            boxes.append(tuple(int(i) for i in input().split()))
            if boxes[-1] == (-1, -1):
                boxes.pop()
                break
        max_w = 0
        total_h = 0
        cur_w = 0
        cur_h = 0

        for w,h in boxes:
            # Does not fit in row
            if (cur_w + w > m):
                max_w = max(max_w, cur_w)
                total_h += cur_h
                cur_w = 0
                cur_h = 0

            cur_w += w
            cur_h = max(cur_h,h)

        final_w = max(max_w, cur_w)
        final_h = total_h + cur_h
        print(f"{final_w} x {final_h}")

if __name__ == "__main__":
    main()

