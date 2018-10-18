"""
/*  Turner Atwood
 *  10/13/18
 *  Candy Division Run [3.5]: (https://open.kattis.com/problems/candydivision)
 *	Simple find the divisors of a number problem
 */ 
"""

from math import sqrt

def main():
	num = int(input())
	upper_limit = int(sqrt(num))
	# Divisors must be in order, so using two lists lets
	# 	us avoid expensive sorts or insertions 
	front = []
	back = []
	for i in range(1, upper_limit+1):
		if num%i == 0:
			front.append(str(i-1))
			back.append(str(num//i-1))
			# Only include the square root once
			if i == sqrt(num):
				front.pop()
				
	print(" ".join(front) +  " " + " ".join(back[::-1]))


if __name__ == "__main__":
	main()