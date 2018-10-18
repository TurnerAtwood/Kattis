"""
/*	Turner Atwood
 *	10/15/18
 *	T9 Spelling [https://open.kattis.com/problems/t9spelling] (1.9)
 *	The worst part was typing the reference dict
 */
"""

pad = {'a':'2', 'b':'22', 'c':'222', 'd':'3', 'e':'33', 'f':'333', 'g':'4', 'h':'44', 'i':'444', 'j':'5', 'k':'55', 'l':'555', 'm':'6', 'n':'66', 'o':'666', 'p':'7', 'q':'77', 'r':'777', 's':'7777', 't':'8', 'u':'88', 'v':'888', 'w':'9', 'x':'99', 'y':'999', 'z':'9999', ' ':'0'}

def main():
	num_cases = int(input())
	for cnum in range(num_cases):
		letters = [i for i in input()]
		key_presses = []
		last = ''
		# Linear scan over the letters typed
		for let in letters:
			new_key = pad[let]
			# Add a space on consective letters using the same button
			if new_key[0] == last:
				key_presses.append(" " + new_key)
			else:
				key_presses.append(new_key)

			# 0 acts slightly different from other buttons
			if new_key == 0:
				last = 0
			else:
				last = new_key[0]

		# Slightly messy output ~python~
		print(f"Case #{cnum+1}:", "".join(key_presses))

if __name__ == "__main__":
	main()