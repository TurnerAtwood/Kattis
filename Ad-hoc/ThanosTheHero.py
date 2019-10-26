"""
/*	Turner Atwood
 *	4/9/19
 *	Thanos The Hero [3.8] https://open.kattis.com/problems/thanosthehero
 *	Ad-hoc : Iterate over the list backwards
 */
"""

def main():
	N = int(input())
	planets = [int(i) for i in input().split()]
	planets = planets[::-1]
	count = 0
	for i in range(N-1):
		a = planets[i]
		b = planets[i+1]
		if a > b:
			continue
		if a == 0:
			count = 1
			break
		count += (b-a+1)
		planets[i+1] = a-1
	print(count)

if __name__ == "__main__":
	main()