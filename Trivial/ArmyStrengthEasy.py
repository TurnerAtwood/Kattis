"""
/*	Turner Atwood
 *	10/20/18
 *	Army Strength (easy) [2.1] https://open.kattis.com/problems/armystrengtheasy
 *	Ad-hoc 
 */
"""

def main():
	input()
	G,M = [int(i) for i in input().split()]
	god = [int(i) for i in input().split()]
	god.sort(reverse=True)
	mech = [int(i) for i in input().split()]
	mech.sort(reverse=True)

	while(god and mech):
		a = god[-1]
		b = mech[-1]
		if a < b:
			del(god[-1])
		else:
			del(mech[-1])
	if god:
		print("Godzilla")
	else:
		print("MechaGodzilla")

if __name__ == "__main__":
	T = int(input())
	for i in range(T):
		main()