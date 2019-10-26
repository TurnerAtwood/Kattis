"""
/*	Turner Atwood
 *	10/21/19
 *	Digits [4.1] https://open.kattis.com/problems/digits
 *	Ad-hoc: Repeatedly take the length of the lengths of input
 */
"""

def main():
	while True:
		line = input()
		if line == "END":
			break

		# Remove any leading zeros
		digits = list(line)[::-1]
		while len(digits) > 1 and digits[-1] == "0":
			digits.pop()
		digits = digits[::-1]

		if digits == ["0"]:
			print(2)
			continue
		if digits == ["1"]:
			print(1)
			continue

		# Take the length of the int until that equals 1
		count = 2
		n = len(digits)
		while (n > 1):
			count += 1
			n = len(str(n))
		print(count)

if __name__ == "__main__":
	main()