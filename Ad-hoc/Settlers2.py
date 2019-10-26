"""
/*	Turner Atwood
 *	10/23/19
 *	Settlers of Catan [4.3] https://open.kattis.com/problems/settlers2
 *	Ad-hoc : Generate the tiles based on the rules using a queue
 */
"""
from math import inf

def main():
	RES_LIST = [1,2,3,4,5]

	N = int(input())
	reqs = [int(input()) for i in range(N)]
	highest = max(reqs)


	#          0 1 2 3 4 5 6 7 8
	res_at = [-1,1,2,3,4,5,2,3]
	res_freq = [-1, 1, 2, 2, 1, 1]

	q = [(2,3),(3,3),(4,3),(5,3),(6,3),(7,3)]
	for i in range(8,highest+1):
		neighs = [i-1,q[0][0]]
		q[-1] = (q[-1][0],q[-1][1]+1)
		q[0] = (q[0][0],q[0][1]+1)
		if q[0][1] == 6:
			del(q[0])
			q[0] = (q[0][0],q[0][1]+1)
			neighs.append(q[0][0])
		q.append((i,len(neighs)))
		

		# Handle Resources
		neigh_res = [res_at[i] for i in neighs]
		pot_res = [i for i in RES_LIST if i not in neigh_res]
		pot_res = {i:res_freq[i] for i in pot_res}
		lowest_val = inf
		lowest_list = []
		for res in pot_res:
			if pot_res[res] < lowest_val:
				lowest_val = pot_res[res]
				lowest_list = [res]
			if pot_res[res] == lowest_val:
				lowest_list.append(res)
		i_res = sorted(lowest_list)[0]

		res_at.append(i_res)
		res_freq[i_res] += 1

	for req in reqs:
		print(res_at[req])


if __name__ == "__main__":
	main()