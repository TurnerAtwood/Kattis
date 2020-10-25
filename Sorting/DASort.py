"""
/*  Turner Atwood
 *  10/24/2020
 *  DA-Sort [3.0] open.kattis.com/problems/dasort
 *  Iterate backwards to find all elements that come before smaller others.
 ** Also count all elements that would have to be moved after moving those.
 */
"""

from math import inf

def main():
    N = int(input())
    for step in range(N):
        # Input
        _,size = [int(num) for num in input().split()]
        nums = list()
        while len(nums) != size:
            nums += [int(num) for num in input().split()]

        s_nums = sorted(nums)
        count = 0

        # Find everything that must be moved by going from the end
        unmarked_indices = {i for i in range(size)}
        min_seen = inf
        min_marked = inf
        marked = list()

        for i in range(size-1,-1,-1):
            num = nums[i]
            min_seen = min(min_seen, num)
            if num > min_seen:
                marked.append(num)
                min_marked = min(min_marked, num)
                unmarked_indices.remove(i)

        for unm_ind in list(unmarked_indices):
            num = nums[unm_ind]
            if num > min_marked:
                unmarked_indices.remove(unm_ind)

        print(step+1, size - len(unmarked_indices))


if __name__ == "__main__":
    main()

