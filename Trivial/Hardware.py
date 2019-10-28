"""
/*	Turner Atwood
 *	10/27/19
 *	Hardware [2.1] https://open.kattis.com/problems/hardware
 *	Ad-hoc : Trivial
 */
"""
def countDig(num, digits):
	num = str(num)
	for digit in num:
		digits[ord(digit) - ord('0')] += 1

def main():
	N = int(input())
	for z in range(N):
		road_name = input()
		addresses_str = input()
		M = int(addresses_str.split()[0])
		digits = [0 for _ in range(10)]
		
		used = 0
		while (M != used):
			line = input()
			if line[0] == "+":
				line = line.split()
				# Loop over the interval
				cur = int(line[1])
				last = int(line[2])
				step = int(line[3])
				while (cur <= last):
					countDig(cur,digits)
					cur += step
					used += 1
			else:
				used += 1
				countDig(int(line),digits)

		# OUTPUT
		output = []
		output.append(road_name)
		output.append(addresses_str)
		for i in range(10):
			output.append(f"Make {digits[i]} digit {i}")
		total = sum(digits)
		if total == 1:
			output.append(f"In total {sum(digits)} digit")
		else:
			output.append(f"In total {sum(digits)} digits")

		print("\n".join(output))

if __name__ == "__main__":
	main()