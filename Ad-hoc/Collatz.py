"""
/*	Turner Atwood
 *	9/22/18
 *	Collatz Conjecture [4.3]: (https://open.kattis.com/problems/collatz)
 *	Go through collatz sequences in reverse to find where they diverge
 */		
"""
# Compute the collatz sequence of a number
def _collatz(num):
	series = []
	while num > 1:
		series.append(num)
		if num%2 == 0:
			num = num//2
		else:
			num = 3*num +1
	return series

def main():
	while True:
		x,y = [int(num) for num in input().split(" ")]
		# 0 0 denotes the end  of the program
		if x == 0 and y == 0:
			break
		# Compute the sequences and reverse them
		seq_x = _collatz(x)[::-1]
		seq_y = _collatz(y)[::-1]
		# Compute how many of the last elements are the same
		##	The last element they differ in is where they 'meet'
		count = 0
		meet = 1
		for (a,b) in zip(seq_x, seq_y):
			if not a == b:
				break
			count += 1
			meet = a

		# Formatting Output
		output =  f"{x} needs {len(seq_x)-count} steps, "
		output += f"{y} needs {len(seq_y)-count} steps, "
		output += f"they meet at {meet}"
		print(output)

if __name__ == "__main__":
	main()