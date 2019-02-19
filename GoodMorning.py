"""
/*	Turner Atwood
 *	2/18/19
 *	Good Morning [3.0]: (https://open.kattis.com/problems/goodmorning)
 *	Finds all possible reachable numbers
 */
 """

# Build the adjacency lists of each button
## More fun than hard coding each list
def build_btn():
	btn = dict()
	btn[0] = {0}
	btn[9] = {9}
	for i in range(8,0,-1):
		btn[i] = {i}
		if not i in [3,6]:
			btn[i] = btn[i].union(btn[i+1])
		if not i in [7]:
			btn[i] = btn[i].union(btn[(i+3)%11])
	return btn

# Build every reachable number of 3 digits
def build_possible():
	DIGITS = 3
	btn = build_btn()
	possible = {i for i in range(10)}
	for i in range(DIGITS-1):
		new_poss = set()
		for num in possible:
			last_digit = num%10
			for next_digit in btn[last_digit]:
				new_poss.add(num*10+next_digit)
		possible = possible.union(new_poss)
	return sorted(possible)

# Find the closest element using a binary search
def bin_search(look, possible):
	low_index = 0
	high_index = len(possible)
	while not low_index == high_index:
		middle_index = (high_index+low_index)//2
		if look >= possible[middle_index]:
			low_index = middle_index
		else:
			high_index = middle_index
		if high_index - low_index < 2:
			break
	high_diff = possible[high_index] - look
	low_diff =  look - possible[low_index]
	if low_diff < high_diff:
		return possible[low_index]
	return possible[high_index]

def main():
	possible = build_possible()
	N = int(input())
	for i in range(N):
		look = int(input())
		print(bin_search(look, possible))


if __name__ == "__main__":
	main()
