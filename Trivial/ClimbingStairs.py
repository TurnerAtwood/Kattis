"""
/*  Turner Atwood
 *  9/20/2021
 *  Climbing Stairs [4.2] : (https://open.kattis.com/problems/climbingstairs)
 *  Ad-hoc - Go to work, then to the reg desk, go up and down until we reach n, then walk down and out
 */
"""

def main():
    n,r,k = (int(i) for i in input().split())

    steps = k + abs(r-k) # Work on k then move to r
    if (n > steps):
        steps += (n - steps) + (n - steps)%2
    steps += r

    print(steps)

if __name__ == "__main__":
    main()

