"""
/*  Turner Atwood
 *  10/16/2020  (Updated from 2016)
 *  Zigzag [5.0] open.kattis.com/problems/zigzag2
 *  Ad-hoc: Just track how many times the entire list
 ** flips between increasing and decreasing
 */
"""

import os
def main():
    nums = [int(item) for item in os.read(0, 100000000).split()[1:]]
    nums = nums[0:1] + [nums[i] for i in range(1,len(nums)) if nums[i] != nums[i-1]]
    total = min(2, len(nums))
    for i in range(len(nums)-2):
        total += ( (nums[i] > nums[i+1]) == (nums[i+2] > nums[i+1]) )
    print(total)

if __name__ == "__main__":
    main()

