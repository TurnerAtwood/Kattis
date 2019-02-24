/*	Turner Atwood
 *	2/19/19
 *	Reachable Roads [2.4] : (https://open.kattis.com/problems/reachableroads)
 *	UnionFind
 */

import java.util.*;

class ReachableRoads {
	
	static int[] nodes;
	static int M;

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		for (int z = 0; z < N; z++) {
			// Reinitialize the union-find
			M = in.nextInt();
			nodes = new int[M];
			for (int i = 0; i < M; i++) {
				nodes[i] = i;
			}

			// Get the endpoints and union them together
			int R = in.nextInt();
			for (int i = 0; i < R; i++) {
				union(in.nextInt(), in.nextInt());
			}
			// Find on each endpoint and count disjoint sets
			
			HashSet<Integer> groups = new HashSet<Integer>();

			for (int i = 0; i < M; i++) {
				groups.add(find(i));
			}
			
			System.out.println(groups.size()-1);
		}
	}

	static void union(int a, int b) {
		int parentA = find(a);
		int parentB = find(b);
		// Union the larger parent to the smaller parent's set
		if (parentA < parentB) {
			nodes[parentA] = parentB;
		}
		else {
			nodes[parentB] = parentA;
		}
		
	}

	static int find(int a) {
		if (nodes[a] != a) {
			nodes[a] = find(nodes[a]);
		}
		return nodes[a];
	}
}