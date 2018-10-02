"""
/*	Turner Atwood
 *	10/1/18
 *	All About that Base [2.9] (https://open.kattis.com/problems/allaboutthatbase)
 */
"""
POSSIBLE_BASES = [str(i) for i in range(1,10)] + [chr(i) for i in range(97,123)]
DIGIT_VALUES = {j:i+1  for i,j in enumerate(POSSIBLE_BASES)}
DIGIT_VALUES['0'] = 0
POSSIBLE_BASES = {i+1:j for i,j in enumerate(POSSIBLE_BASES)}
POSSIBLE_BASES[36] = '0'
# print(DIGIT_VALUES)
# print(POSSIBLE_BASES)

def _str_base_to_decimal(base, number_str):
	power = 1
	total = 0
	if (base  == 1):
		if not set(number_str) == {'1'}:
			return -1
		return len(number_str)
	for digit in number_str[::-1]:
		digit_value = DIGIT_VALUES[digit]
		if base <= digit_value:
			return -1
		total += power * digit_value
		power *= base
	return total 

def _perform_operation(num_a, num_b, op):
	if op == "+":
		result = num_a + num_b
	elif op == "-":
		result = num_a - num_b
	elif op == "*":
		result = num_a * num_b
	else:
		result = num_a / num_b
	return result

def main():
	num_cases = int(input())
	for _ in range(num_cases):
		in_line = input().split(" ")
		nums = in_line[::2]
		op = in_line[1]
		found_bases = []
		# Try all of the bases
		for base in POSSIBLE_BASES:
			num_in_decimal = [_str_base_to_decimal(base, num) for num in nums]
			result = _perform_operation(num_in_decimal[0], num_in_decimal[1], op)
			if -1 in num_in_decimal:
				continue
			elif not result == num_in_decimal[2]:
				continue
			else:
				found_bases.append(POSSIBLE_BASES[base])
		if not found_bases:
			print("invalid")
		else: 
			print("".join(found_bases))





if __name__ == "__main__":
	main()
