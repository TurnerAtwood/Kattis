"""
/*	Turner Atwood
 *	10/16/18
 *	Meow Factor [3.8] (https://open.kattis.com/problems/meowfactor)
 *	Slight twist on finding all factors
 */
"""

from math import sqrt

def main():
	num = int(input())

	meow = 1
	check_num = 1
	# The search space needs to be as small as possible
	while True:
		val = check_num**9
		if val > num:
			break
		if num%(int(val)) == 0:
			meow = check_num
		check_num += 1
	print(meow)

if __name__ == "__main__":
	main()