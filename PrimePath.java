/*	Turner Atwood
 *	2/25/19
 *	Prime Path [2.2] : (https://open.kattis.com/problems/primepath)
 *	BFS over 4-digit prime numbers
 **	A neighbor of a prime is any other prime that differs by only 1 digit
 **	Likely overengineered for the given problem, but easily scalable
 */

import java.util.*;

class PrimePath {
	static boolean[] siev;
	static int DIGITS = 4;
	static int MAX = (int) Math.pow(10, DIGITS);

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		buildSiev();

		int N = in.nextInt();
		for (int z = 0; z < N; z++) {
			int start = in.nextInt();
			int target = in.nextInt();
			//BFS:
			// Add the distance of a prime to the map when it is visited
			HashMap<Integer, Integer> distances = new HashMap<Integer, Integer>();
			LinkedList<Integer> queue = new LinkedList<Integer>();
			queue.addLast(start);
			distances.put(start,0);
			while (!queue.isEmpty()) {
				int current = queue.pollFirst();
				int cur_dist = distances.get(current);
				if (current == target) {
					System.out.println(cur_dist);
					break;
				}

				//Try all prime neighbors
				int power = 1;
				for (int i = 0; i < DIGITS; i++) {
					int rem_i_dig = current/(power*10)*(power*10) + current%power;
					//System.out.println(current + ": " + rem_i_dig + "+ " + power + "*j");
					for (int j = 0; j <= 9; j++) {
						int newNum = rem_i_dig + j*power;
						if (newNum >= MAX/10 && siev[newNum] && !distances.containsKey(newNum)) {
							distances.put(newNum, cur_dist + 1);
							queue.addLast(newNum);
						}
					}
					power *= 10; 
				}
			}
		}
	}

	// Standard siev of eratosthenes
	static void buildSiev() {
		siev = new boolean[MAX];
		Arrays.fill(siev, true);
		siev[0] = false;
		siev[1] = false;
		int i = 1;
		while (i*i < MAX) {
			i++;
			if (!siev[i]) {
				continue;
			}

			for (int j = i*i; j < MAX; j += i) {
				siev[j] = false;
			}
		}
	}
}