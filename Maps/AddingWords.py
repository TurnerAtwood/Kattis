"""
/*	Turner Atwood
 *	9/5/18
 *	Adding Words [4.3]: (https://open.kattis.com/problems/addingwords)
 *	Use a map from num -> word and a map from word -> num
 ** word -> num for + or -, and num -> word for the definition of the result
 **	This is the most efficient solution, since all access are O(1).
 */	
"""
import sys

def main(): 
	# Define the maps for both directions
	word_to_num = {}
	num_to_word = {}
	for line in sys.stdin:
		line = line.rsplit()
		# Assign a new value to a word (will overwrite any previous definion)
		if line[0] == "def":
			word = line[1]
			num = (int)(line[2])
			# Changing a definiton requires clearing the previous def
			if word in word_to_num:
				tmp_num = word_to_num[word]
				del word_to_num[word]
				del num_to_word[tmp_num]
			# Store the translation in both maps
			word_to_num[word] = num
			num_to_word[num] = word
		# Clear all stored definitions
		elif line[0] == "clear":
			word_to_num.clear()
			num_to_word.clear()
		# Use definitions to perform + or - and print unknown if any part fails
		else:
			# Grab all of the operations used (+/-/=) - found at (1,3,5,...)
			ops = line[2:][::2]
			# Ensure that every operand has a word definition
			try:
				vals = [word_to_num[word] for word in line[1:][::2]]
			except KeyError as err:
				ops = []
				result = "unknown"
			else:
				# Get result and feed it into num_to_word
				# Use the list of vals as a stack 
				for op in ops:
					if op == "+":
						vals[0] = vals[0] + vals[1]
						vals.pop(1)
					elif op == "-":
						vals[0] = vals[0] - vals[1]
						vals.pop(1)
					else:
						result = vals.pop()
			# Ensure the result has a definition 
			if result in num_to_word:
				result = num_to_word[result]
			else:
				result = "unknown"
			# Formatting output
			line = line[1:] + [result]
			print(" ".join(line))

if __name__ == "__main__":
	main()
