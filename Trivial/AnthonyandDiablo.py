"""
/*	Turner Atwood
 *	10/16/19
 *	Anthony and Diablo [2.5] https://open.kattis.com/problems/anthonyanddiablo
 *	Ad-hoc : A circle provides optimal pperimeter:area
 */
"""

pi = 3.14159265358979323

def main():
	A,N = [float(i) for i in input().split()]
	rad = N/(2*pi)
	area = pi*rad*rad

	if area > A:
		print("Diablo is happy!")
	else:
		print("Need more materials!")

if __name__ == "__main__":
	main()