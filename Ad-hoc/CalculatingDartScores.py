"""
/*	Turner Atwood
 *	9/6/18
 *	Calculating Dart Scores [2.7] : (https://open.kattis.com/problems/calculatingdartscores)
 *	Brute force - try every possible combo of 1 and 2 throws
 **	3 throws is only doable by reducing the  initial amount as much as possible
 */	
"""
# Build the ranges of unique scores for each area
drange = range(1,21,1)
single = [i for i in drange]
double = [2*i for i in drange if 2*i not in single]
triple = [3*i for i in drange if 3*i not in single and 3*i not in double]


def main():
	num = (int)(input())
	_two_throw(num)
	output = []
	while(num > 0):
		last_throw = _one_throw(num)
		if (last_throw):
			output += [last_throw]
			num = 0
			break
		# 120 or over => drop the score to the range of two throws
		elif num >= 120:
			output += ["triple 20"]
			num -= 60
		# Try to get num in two throws
		else:
			# Try tow throws
			two_result = _two_throw(num)
			if (two_result):
				output += two_result
				num = 0
			# If this is reached there is ann issue
			else:
				output += ["triple 20"]
				num -= 60
	# Make sure it can be done in 3 or fewer throws
	if len(output) > 3 or num != 0:
		print("impossible")
	else:
		print("\n".join(output))

# Return how (if possible) to get target in one throw
def _one_throw(target):
	if target in single:
		return(f"single {target}")
	if target in double:
		return(f"double {target//2}")
	if target in triple:
		return(f"triple {target//3}")
	return False

# Return how (if possible) to get target in two throws
def _two_throw(target):
	tot = single + double + triple
	# Every combo of two throws
	tot = [(i,j) for i in tot for j in tot if i+j == target]
	if not tot:
		return False
	return([_one_throw(num) for num in tot[0]])


if __name__ == "__main__":
	main()
