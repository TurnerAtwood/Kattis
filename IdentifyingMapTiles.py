"""
/*	Turner Atwood
 *	9/22/18
 *	Identifying Map Tiles [1.6]: (https://open.kattis.com/problems/maptiles2)
 */	
"""
def main():
	quadkey = input()
	zoom = len(quadkey)
	count = 0
	spot = [0,0]
	for digit in quadkey[::-1]:
		dig = int(digit)
		spot = [spot[0]+dig%2*2**count, spot[1]+dig//2*2**count]
		count += 1
	print(zoom, spot[0], spot[1])

if __name__ == "__main__":
	main()