"""
/*	Turner Atwood
 *	9/5/18
 *	Guessing Game [2.9]: (https://open.kattis.com/problems/guessinggame)
 */	
"""

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
	past_pairs = {}
	answer = 0
	while (True):
		num = int(input())
		if num == 0:
			break 

		response = input()

		if num in past_pairs:
			if not response == past_pairs[num]:
				liar = True

		past_pairs[num] = response

		if response == "right on":
			liar = liar or _check_map(past_pairs, num)
			if liar:
				print("Stan is dishonest")
			else:
				print("Stan may be honest")
			liar = False
			past_pairs = {}

if __name__ == "__main__":
	main()