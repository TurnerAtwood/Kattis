"""
/*	Turner Atwood
 *	10/2/18
 *	Bing it On [4.1] (https://open.kattis.com/problems/bing)
 *	Prefix Tree
 */
"""

# TOOO SLOWWWWW

class Node():
	count = 0
	children = None
	val = None

	def __init__(self, letter):
		self.count = 1
		self.val = letter
		self.children = set()

	def _find(self, match_letter):
		for potential_node in self.children:
			if potential_node.val == match_letter:
				return potential_node
		return None

class PrefixTree():
	root = None

	def __init__(self, letters):
		first_letter = letters[0]
		self.root = Node(None)
		self._add_to_tree(letters, self.root)

	# Only add once a str has been searched
	def _add_to_tree(self, letters, current_parent):
		# letters = letters.copy()
		while letters:
			letter = letters.pop(0)
			new_node = Node(letter)
			current_parent.children.add(new_node)
			current_parent = new_node

	# Return letters not found and reference node
	def _is_prefix(self, letters, do_add = True):
		current_node = self.root
		# letters = letters.copy()
		while letters:
			match_letter = letters[0]
			next_node = current_node._find(match_letter)
			if next_node:
				letters = letters[1:]
				if do_add:
					current_node.count += 1
				current_node = next_node
			else:
				break
		if do_add:
			current_node.count += 1	
		return (letters, current_node)





def main():
	num_words = int(input())
	pTree = None
	output = ""
	for _ in range(num_words):
		letters = list(input())
		if not pTree:
			pTree = PrefixTree(letters)
			output += '0\n'
		else:
			leftovers, last_node = pTree._is_prefix(letters)
			if not leftovers:
				output += f"{last_node.count-1}\n"
			else:
				pTree._add_to_tree(leftovers, last_node)
				output += '0\n'
	print(output)

if __name__ == "__main__":
	main()
