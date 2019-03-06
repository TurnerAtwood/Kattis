"""
/*	Turner Atwood
 *	9/22/18
 *	Daydreaming Stockbroker [3.1]: (https://open.kattis.com/problems/stockbroker)
 *	Ad-hoc - Decide what to do each day based off of the next day
 */	
"""

def main():
	num_days = int(input())
	money = 100
	shares_held = 0
	
	# Build the input array
	price_list = []
	while(True):
		try:
			price_list.append(int(input()))
		except:
			break

	# On any day: Sell if today > tomo, otherwise TRY to buy
	for i in range(0, len(price_list)-1):
		current_price = price_list[i]
		next_price = price_list[i+1]

		peak = current_price > next_price
		# SELL
		if peak and shares_held > 0:
			money += shares_held * current_price
			shares_held = 0
		
		# BUY
		if not peak and shares_held == 0:
			shares_held = min(100000, money//current_price)
			money -= current_price*shares_held

	# Dump any remaining stocks
	final_price = price_list[-1]
	if final_price > 0:
		money += shares_held * final_price
		shares_held = 0

	# Output
	print(money)


if __name__ == "__main__":
	main()