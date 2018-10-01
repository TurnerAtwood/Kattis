"""
/*	Turner Atwood
 *	9/22/18
 *	Daydreaming Stockbroker [3.2]: (https://open.kattis.com/problems/stockbroker)
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

	for i in range(0, len(price_list)-1):
		current_price = price_list[i]
		next_price = price_list[i+1]

		peak = current_price > next_price
		if peak and shares_held > 0:
			# SELL
			money += shares_held * current_price
			shares_held = 0
		
		if not peak and shares_held == 0:
			# BUUUUY
			shares_held = min(100000, money//current_price)
			money -= current_price*shares_held
	final_price = price_list[-1]
	if final_price > 0:
		# print("selling at:", final_price)
		money += shares_held * final_price
		shares_held = 0

	print(money)


if __name__ == "__main__":
	main()