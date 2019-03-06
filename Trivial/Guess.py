"""
/*	Turner Atwood
 *	10/28/18
 *	Guess the Number [3.2] (https://open.kattis.com/problems/guess)
 */
"""

# Standard Binary Search
# 	Find a number between 1 and 1000 in 10 guesses
def main(): 
	high = 1001
	low = 0
	while True:
		# Make a guess
		guess = low + (high-low)//2
		print(guess)

		# Update the bounds for the search
		response = input()
		if response == "lower":
			high = guess
		elif response == "higher":
			low = guess
		else:
			break	

if __name__ == "__main__":
	main()