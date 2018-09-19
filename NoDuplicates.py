"""
/*	Turner Atwood
 *	9/5/18
 *	No Duplicates [1.3]: (https://open.kattis.com/problems/nodup)
 */	
"""
if __name__ == "__main__":
	main()
	
def main():
	inp = input().split(" ")
	words = {}
	passed = True
	for word in inp:
		if word in words:
			passed = False
			print("no")
			break
		else:
			words[word] = 0
	if passed: print("yes")
