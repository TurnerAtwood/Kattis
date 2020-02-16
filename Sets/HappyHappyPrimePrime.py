"""
/*	Turner Atwood
 *	2/16/20
 *	Happy Happy Prime Prime [2.5] https://open.kattis.com/problems/happyprime
 *	Sets : Use sets to detect eventually periodic "happy" sequences
 */
"""

seen = set()

def main():
	siev = make_siev()
	P = int(input())

	for index in range(1,P+1):
		_,m = [int(i) for i in input().split()]
		bad = True

		if not siev[m]:
			bad = False
		if siev[m] and is_happy(m, set()):
			print(f"{index} {m} YES")
		else:
			print(f"{index} {m} NO")

def is_happy(m, seen):
	total = 0
	while m > 0:
		total += (m%10)*(m%10)
		m = m // 10
	if total in seen:
		return False
	seen.add(total)

	if total == 1:
		return True
	if total == 0:
		return False
	return is_happy(total,seen)


LIMIT = 10001
def make_siev():
	siev = [True for i in range(LIMIT)]
	siev[1] = False
	for i in range(2,int(LIMIT**(0.5))):
		if siev[i]:
			for j in range(i*i,LIMIT,i):
				siev[j] = False
	return siev

if __name__ == "__main__":
	main()