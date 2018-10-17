"""
/*	Turner Atwood
 *	10.7.18
 *	Mixed Fractions [1.5] (https://open.kattis.com/problems/mixedfractions)
 */
"""

def main():
	while True:
		top, bot = [int(num) for num in input().split(" ")]
		if bot == 0:
			break
		num = top//bot
		top = top - bot*num
		print(num, top, "/", bot)

if __name__ == "__main__":
	main()