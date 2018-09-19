"""
/*	Turner Atwood
 *	9/8/18
 *	Touchscreen Keyboard [2.0]: (https://open.kattis.com/problems/touchscreenkeyboard)
 */	
"""

def _distance_between_keys(key1, key2):
	key1 = keyboard[key1]
	key2 = keyboard[key2]
	distance = abs(key1[0]-key2[0])+abs(key1[1]-key2[1])
	return distance

def _distance_between_words(word1, word2):
	distance = 0
	for key1,key2 in zip(word1,word2):
		distance += _distance_between_keys(key1, key2)
	return distance

def main():
	# Get number of test cases
	cases = (int)(input())
	for trash in range(cases):
		# Get rest of setup input
		inp_line = input().split(" ")
		base_word = inp_line[0]
		num_words = (int)(inp_line[1])
		
		# Get words and their distance as they come in
		words = []
		for i in range(num_words):
			word = input()
			words.append((_distance_between_words(base_word, word), word))
		
		# Sort and print results
		words = sorted(words)
		[print(word[1], word[0]) for word in words]

# Create global keyboard
def _build_keyboard():
	lines = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
	keyboard = {}
	for line_ind,line in enumerate(lines):
		for letter_ind,letter in enumerate(line):
			keyboard[letter] = (line_ind,letter_ind)
	return keyboard
keyboard = _build_keyboard()

if __name__ == "__main__":
	main()