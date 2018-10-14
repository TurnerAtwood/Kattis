"""
/*	Turner Atwood
 *	10/13/18
 *	Bits [2.7] (https://open.kattis.com/problems/bits)
 *
 */
"""

def main():
	for _ in range(int(input())):
		num_str = input()
		max_ones = 0
		for i in range(1, len(num_str)+1):
			look_str = num_str[0:i]
			max_ones = max(max_ones, bin(int(look_str)).count('1'))
		print(max_ones)


if __name__ == "__main__":
	main()