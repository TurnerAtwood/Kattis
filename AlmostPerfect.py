"""
/*	Turner Atwood
 *	9/22/18
 *	Almost Perfect [3.5]: (https://open.kattis.com/problems/almostperfect)
 */	
"""
import math

def _list_of_divisors(num):
	limit = int(math.sqrt(num))+1
	divisor_list = set()
	divisor_list.add(1)
	for i in range(2, limit):
		if num%i == 0:
			divisor_list.add(i)
			divisor_list.add(num//i)
	return divisor_list

def main():
	while True:
		try:
			number = int(input())
		except:
			break
		divisor_list = _list_of_divisors(number)
		div_total = sum(divisor_list)
		div_total_diff = abs(div_total - number)
		if div_total_diff == 0:
			print(f"{number} perfect")
		elif div_total_diff <= 2:
			print(f"{number} almost perfect")
		else:
			print(f"{number} not perfect")


if __name__ == "__main__":
	main()