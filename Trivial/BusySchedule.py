"""
/*	Turner Atwood
 *	3/??/19
 *	Busy Schedule [2.5] : (https://open.kattis.com/problems/busyschedule)
 *	Trivial Sorting and data manipulation
 */
"""
def main():
	N = int(input())
	while N != 0:
		times = []
		for i in range(N):
			line = input()
			key = line
			line = line.split(":")
			time = int(line[0])%12*60
			line = line[1].split(" ")
			time += int(line[0])
			if line[1] == "p.m.":
				time += 60*12 
			times += [(time, key)]
		times = sorted(times)
		
		[print(i[1]) for i in times]
		N = int(input())
		if N != 0:
			print("")


if __name__ == "__main__":
	main()