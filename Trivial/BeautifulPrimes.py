"""
/*  Turner Atwood
 *  9/11/2021
 *  Beautiful Primes [4.3] (https://open.kattis.com/problems/beautifulprimes)
 *  Ad-hoc - Just binary search the number of 7's and 11's to get the product to have N digits
 */
"""

from math import log

def main():
    N = int(input())
    if digit_num(N, 0) == N:
        return ((N, 0))
    
    low,high = 0,N
    while low < high-1:
        mid = (high+low)//2
        mid_val = digit_num(mid, N-mid)
        if mid_val == N:
            return ((mid, N-mid))
        if mid_val < N:
            high = mid
        else:
            low = mid

    low += 1
    return ((low, N-low))

def digit_num(ct_7, ct_11):
    prod = (7**ct_7) * (11**ct_11)
    return len(str(prod))

def final_output(ct_7, ct_11, *args):
    num_list = ["7"]*ct_7 + ["11"]*ct_11
    return " ".join(num_list)

if __name__ == "__main__":
    for _ in range( int(input()) ):
        print( final_output(*main()) )

