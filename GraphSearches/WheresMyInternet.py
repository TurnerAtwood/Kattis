"""
/*	Turner Atwood
 *	9/6/18
 *	Where's My Internet?? [3.3]: (https://open.kattis.com/problems/wheresmyinternet)
 *	UNIONFIND - This is old, I would never write it this way again
 */	
"""

houses = []

def main():
	inp = input().split(" ")
	houses = [i for i in range((int)(inp[0])+1)]
	
	# Returns the root and compresses the entire path
	def _find(visited, val): 
		# Cycle back or already root
		if houses[val] != val or val in visited:
			houses[val] = _find(visited, houses[val])
		visited += [val]
		return houses[val]

	wires = (int)(inp[1])
	for i in range(wires):
		inp = input().split(" ")
		first, second = (int)(inp[0]),(int)(inp[1])
		# Trying to make sure links aren't overwritten
		old_root = _find([], houses[first])
		houses[first] = _find([], houses[second])
		houses[old_root] = houses[first]

	root = _find([], 1)
	separate = [str(i) for i in range(1, len(houses)) if not _find([], i) == root]
	if not separate:
		print("Connected")
	else:
		print("\n".join(separate))


if __name__ == "__main__":
	main()