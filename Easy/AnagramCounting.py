"""
/*	Turner Atwood
 *	10/29/18
 *	Anagram Counting [3.2] (https://open.kattis.com/problems/anagramcounting)
 *	Standard calculation of the permutations of the letters in a string
 */
"""
from math import factorial

def main():
	while True:
		# One line per test case until the end of the file
		try:
			line = input()
		except:
			break

		# Start with the number of letters factorial
		total = factorial(len(line))
		
		# Find the frequncy of each letter
		letters = dict()
		for letter in line:
			if letter in letters:
				letters[letter] += 1
			else:
				letters[letter] = 1

		# Divide total by the factorial of each frequency
		for letter in letters:
			total  = total // int(factorial(letters[letter]))

		print(int(total))

if __name__ == "__main__":
	main()