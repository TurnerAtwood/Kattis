"""
/*	Turner Atwood
 *	9/22/18
 *	Karte [1.6]: (https://open.kattis.com/problems/karte)
 */	
"""

# Find how many cards you still need for each suit
def main():
	suits = ["P", "K", "H", "T"]
	# Hold a dictionary of String to sets
	deck = {suit:set() for suit in suits}
	line = input()
	failed = False
	#  Try to add each card in the input to its suit's set
	for i in range(0, len(line), 3):
		suit,num = line[i:i+1],line[i+1:i+3]
		if num in deck[suit]:
			failed = True
			break
		else:
			deck[suit].add(num)

	if failed:
		print("GRESKA")
	else:
		lengths = [str(13 - len(deck[suit])) for suit in suits]
		print(" ".join(lengths))


if __name__ == "__main__":
	main()