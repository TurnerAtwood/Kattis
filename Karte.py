"""
/*	Turner Atwood
 *	9/22/18
 *	Karte [1.6]: (https://open.kattis.com/problems/karte)
 */	
"""
def main():
	suits = ["P", "K", "H", "T"]
	deck = {suit:set() for suit in suits}
	line = input()
	failed = False
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