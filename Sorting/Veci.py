"""
/*	Turner Atwood
 *	10/4/18
 *	Veci [1.9] (https://open.kattis.com/problems/veci)
 *	Search the digits from right to left to find the first digit to swap
 **	Swap that digit with the smallest digit to the right of it that is larger
 **	Sort the remaining digits (ascending) and append them
 **	ex: 827731 -> 2 is the spot : from [7,7,3,1] 3 is the best
 **		So: [8] + [3] + [1,2,7,7] = 831277
 */
"""

# Finds the best digit to switch with the given spot
def _find_replacement_digit(digits, spot):
	switch_val = 10
	switch_spot = 0
	spot_val = digits[spot]
	for j in range(spot+1, len(digits)):
		curr_digit = digits[j]
		if curr_digit > spot_val and curr_digit < switch_val:
			switch_val = digits[j]
			switch_spot = j
	return switch_spot, switch_val

def main():
	# Get input and ensure digits arent in descending order
	digits = [int(i) for i in input()]
	if sorted(digits[::-1]) == digits[::-1]:
		print(0)
	else:
		size = len(digits)
		# Find the first spot you can flip
		for i in range(size-2, -1, -1):
			if digits[i] < digits[i+1]:
				spot = i
				switch_spot, switch_val = _find_replacement_digit(digits, spot)
				break
		
		del(digits[switch_spot])
		digits.append(digits[spot])

		result = digits[0:spot] + [switch_val] + sorted(digits[spot+1:])
		print("".join([str(i) for i in result]))

if __name__ == "__main__":
	main()