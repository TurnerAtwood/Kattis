"""
/*	Turner Atwood
 *	10/19/18
 *	Beat the Sread [2.5] (https://open.kattis.com/problems/beatspread)
 */
"""

# Find two numbers given their sum and difference
def main():
	for _ in range(int(input())):
		total,diff = [int(i) for i in input().split(" ")]
		x = (total+diff)//2
		y = total - x

		# Make sure your numbers are possible and correct
		if x+y != total or x-y != diff or y != abs(y):
			print("impossible")
		else:
			print(x,y)
			
if __name__ == "__main__":
	main()