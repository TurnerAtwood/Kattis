"""
/*	Turner Atwood
 *	10/17/19
 *	Permutation Encryption [2.4] https://open.kattis.com/problems/permutationencryption
 *	Ad-hoc : Apply a permutation repeatedly to a message
 */
"""

def main():
	while (True):
		key = input()
		if (key == "0"):
			break

		key = [int(i) for i in key.split()[1:]]
		n = len(key)
		message = list(input())

		# Buffer the end with spaces
		while (len(message)%n != 0):
			message.append(" ")

		m = len(message)
		output = list()
		for i in range(m//n):
			curr = message[n*i:n*(i+1)]
			# Apply the permutation to each slice of the message
			for j in key:
				output.append(curr[j-1])
		output = "".join(output)
		print(f"'{output}'")


if __name__ == "__main__":
	main()