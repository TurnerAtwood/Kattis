"""
/*	Turner Atwood
 *	9/5/18
 *	Server [1.6]: (https://open.kattis.com/problems/server)
 */	
"""

def main():
	line = input().split(" ")
	num = int(line[0])
	time = int(line[1])
	costs = [int(i) for i in input().split(" ")]
	total = 0
	for cost in costs:
		if cost <= time:
			total += 1
			time -= cost
		else:
			break
	print(total)

if __name__ == "__main__":
	main()