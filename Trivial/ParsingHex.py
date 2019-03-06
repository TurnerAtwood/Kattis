"""
/*	Turner Atwood
 *	10/15/18
 *	Parsing Hex [2.9] (https://open.kattis.com/problems/parsinghex)
 */
"""

def main():
	hex_chars = {str(i):i for i in range(10)}
	for i in range(97,103):
		hex_chars[chr(i)] = i-87

	while True:
		# Go until inut stops cooming
		try:
			line = input()
		except:
			break
		
		# Linear scan through the input lines
		hex_nums = []
		for ind in range(0,len(line)-1):
			look = line[ind:ind+2]
			build = []
			# Check if a hex number is starting
			if look == '0x':
				build.append(look)
			if look == '0X':
				build.append(look)
			# Find the whole hex number
			if build:
				ind += 2
				while ind < len(line) and line[ind].lower() in hex_chars:
					build.append(line[ind])
					ind += 1
				hex_nums.append(build)

		# Compute decimal values and print output
		for num in hex_nums:
			result = "".join(num)
			base = 16
			power = 1
			result_val = 0
			for digit in num[1:][::-1]:
				result_val += hex_chars[digit.lower()]*power
				power *= base
			result += " " + str(result_val)
			print(result)				




if __name__ == "__main__":
	main()