"""
/*	Turner Atwood
 *	12/16/19
 *	Missing Numbers [1.7] https://open.kattis.com/problems/missingnumbers
 *	Trivial - Use a set to keep track of the numbers said
 */
"""

def main():
	n = int(input())
	said = set()
	for i in range(n):
		new_number = int(input())
		said.add(new_number)

	high = new_number

	output = []
	for i in range(1, high):
		if i not in said:
			output.append(str(i))

	if output:
		print("\n".join(output))
	else:
		print("good job")

if __name__ == "__main__":
	main()