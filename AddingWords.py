"""
/*	Turner Atwood
 *	9/5/18
 *	Adding Words [3.9]: (https://open.kattis.com/problems/addingwords)
 */	
"""
import sys

def main(): 
	word_to_num = {}
	num_to_word = {}
	for line in sys.stdin:
		line = line.rsplit()
		if line[0] == "def":
			word = line[1]
			num = (int)(line[2])
			if word in word_to_num:
				tmp_num = word_to_num[word]
				del word_to_num[word]
				del num_to_word[tmp_num]
			word_to_num[word] = num
			num_to_word[num] = word
		elif line[0] == "clear":
			word_to_num.clear()
			num_to_word.clear()
		else:
			ops = line[2:][::2]
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
			# print(f"result: {result}")
			if result in num_to_word:
				result = num_to_word[result]
			else:
				result = "unknown"
			line = line[1:] + [result]
			print(" ".join(line))

if __name__ == "__main__":
	main()