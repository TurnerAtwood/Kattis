"""
/* Turner Atwood
 * 11/4/2021
 * Reseto [2.9] (https://open.kattis.com/problems/reseto)
 * Ad-hoc : Run a sieve of Eratosthenes as described
 */
"""

def main():
    N,K = [int(i) for i in input().split()]
    N += 1

    marked = [1]
    primes = [True for i in range(N)]
    for i in range(2, N):
        if not primes[i]:
            continue
        marked.append(i)
        for j in range(i+i, N, i):
            if primes[j]:
                primes[j] = False
                marked.append(j)
    print(marked[K])

if __name__ == "__main__":
    main()

