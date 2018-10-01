"""
/*	Turner Atwood
 *	9/22/18
 *	Almost Perfect [3.4]: (https://open.kattis.com/problems/almostperfect)
 */	
"""
import math

def _sum_of_divisors(num):
	limit = int(math.sqrt(num))
	total = 1
	for i in range(2, limit):
		if num%i == 0:
			total += i
			total += num//i
	return total

def main():
	while True:
		try:
			number = int(input())
		except:
			break
		div_total = _sum_of_divisors(number)
		div_total_diff = abs(div_total - number)
		print(div_total)
		if div_total_diff == 0:
			print(f"{number} perfect")
		elif div_total_diff <= 2:
			print(f"{number} almost perfect")
		else:
			print(f"{number} not perfect")


if __name__ == "__main__":
	main()