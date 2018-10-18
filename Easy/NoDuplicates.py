"""
/*	Turner Atwood
 *	9/5/18
 *	No Duplicates [1.3]: (https://open.kattis.com/problems/nodup)
 */	
"""

# Find if there are duplicates in a list
def main():
	inp = input().split(" ")
	words = set(inp)
	if len(words) == len(inp):
		print("yes")
	else:
		print("no")

if __name__ == "__main__":
	main()
