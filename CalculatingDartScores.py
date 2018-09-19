"""
/*	Turner Atwood
 *	9/6/18
 *	Calculating Dart Scores [2.6]: (https://open.kattis.com/problems/calculatingdartscores)
 */	
"""
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
		# 120 or over => drop by 60
		elif num >= 120:
			output += ["triple 20"]
			num -= 60
		# Try to get num in two throws
		else:
			two_result = _two_throw(num)
			if (two_result):
				output += two_result
				num = 0
			else:
				# May cause problems???
				output += ["triple 20"]
				num -= 60
	if len(output) > 3 or num != 0:
		print("impossible")
	else:
		print("\n".join(output))

def _one_throw(target):
	if target in single:
		return(f"single {target}")
	if target in double:
		return(f"double {target//2}")
	if target in triple:
		return(f"triple {target//3}")
	return False

def _two_throw(target):
	tot = single + double + triple
	tot = [(i,j) for i in tot for j in tot if i+j == target]
	if not tot:
		return False
	return([_one_throw(num) for num in tot[0]])


if __name__ == "__main__":
	main()
