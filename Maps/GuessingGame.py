"""
/*	Turner Atwood
 *	9/5/18
 *	Guessing Game [3.0]: (https://open.kattis.com/problems/guessinggame)
 *	Store responses in a map and check their integrity at the end of each game
 */	
"""

# Make sure that every response is consistant with the answer
def _check_map(responses, answer):
	for key in responses:
		val = responses[key]
		if key < answer and val == "too high":
			return True
		if key > answer and val == "too low":
			return True
	return False

def main():
	liar = False
	# Map of number -> response
	past_pairs = {}
	answer = 0
	while (True):
		num = int(input())
		# End of input at 0
		if num == 0:
			break 

		response = input()

		# If he ever changes his answer for a number he is lying
		if num in past_pairs:
			if not response == past_pairs[num]:
				liar = True

		past_pairs[num] = response

		if response == "right on":
			liar = liar or _check_map(past_pairs, num)
			
			# Output
			if liar:
				print("Stan is dishonest")
			else:
				print("Stan may be honest")
			
			# Reset the game
			liar = False
			past_pairs = {}

if __name__ == "__main__":
	main()