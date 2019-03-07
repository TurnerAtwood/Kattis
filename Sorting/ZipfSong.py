"""
/*	Turner Atwood
 *	10/29/18
 *	Zipf's Song [3.9] (https://open.kattis.com/problems/zipfsong)
 *	Made as short as is reasonable in Python
 **	Just a linear scan and sort on computed value
 */
"""

def main():
	song_num, query_num = [int(i) for i in input().split()]
	scores = []
	for i in range(song_num):
		song = input().split()
		scores += [(-1*int(song[0])*(i+1), i, song[1])] # Package (score,index,name)
	scores = sorted(scores) # Sorts on score then index
	print("\n".join([i[2] for i in scores[:query_num]]))

if __name__ == "__main__":
	main()