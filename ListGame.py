"""
/*	Turner Atwood
 *	9/30/18
 *	A List Game [3.0] (https://open.kattis.com/problems/listgame)
 */
 """

import math

def main():
	num = int(input())
	count = 0
	check = 2
	while check**2 <= num:
		if num%check == 0:
			count += 1
			num /= check
		else:
			check += 1

	print(count+1)
if __name__ == "__main__":
	main()