from sys import stdin

def main():
	# Get n,m and the fish in descending order
	n,m = [int(i) for i in stdin.readline().split()]
	fish = sorted([int(i) for i in stdin.readline().split()], reverse=True)
	# Get the mongers and also sort them
	mongers = []
	for i in range(m):
		mongers.append([int(i) for i in stdin.readline().split()][::-1])
	mongers = sorted(mongers)
	# Go through the fish forward and the fishmongers backward
	total = 0
	for fsh in fish:
		# Add the fish to the highest available price
		total += mongers[-1][0]*fsh
		# Reduce how many fish the last monger wants to purchase by 1
		mongers[-1][1] -= 1
		if mongers[-1][1] == 0:
			# Get rid of a monger who wants no more fish
			del mongers[-1]
		if not mongers:
			break
	print(total)

if __name__ == "__main__":
	main()