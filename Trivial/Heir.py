"""
/*	Turner Atwood
 *	12/16/19
 *	Heir's Dilemma [1.7] https://open.kattis.com/problems/heirsdilemma
 *	Ad-Hoc : 
 */
"""
def numbersInRange(L, H):
    count = 0
    for num in range(L, H+1):
        digits = set(str(num))
        if len(digits) < 6 or '0' in digits:
            continue
        
        good = True
        for digit in digits:
            remainder = num % (int(digit))
            if remainder != 0:
                good = False
                break
        if not good:
            continue

        count += 1
    return count

if __name__ == "__main__":
    L,H = [int(i) for i in input().split()]
    print(numbersInRange(L,H))