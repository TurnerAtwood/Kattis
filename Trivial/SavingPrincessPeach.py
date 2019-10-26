"""
/*	Turner Atwood
 *	10/16/19
 *	Saving Princess Peach [1.8] https://open.kattis.com/problems/princesspeach
 *	Ad-hoc : Trvial Set usage
 */
"""

def main():
	N,Y = [int(i) for i in input().split(" ")]
	found = set()	
	for i in range(Y):
		obs  = int(input())
		if (obs >=0 and obs < N):
			found.add(obs)

	for i in range(N):
		if not i in found:
			print(i)
	print(f"Mario got {len(found)} of the dangerous obstacles.")

if __name__ == "__main__":
	main()