/*	Turner Atwood
 *	3/21/19
 *	Island Hopping [3.4] : (https://open.kattis.com/problems/islandhopping)
 *	Minimum Spanning Tree
 *	Keep in mind everything is just stored in arrays, so it is a little ugly
 */

import java.util.*;

class IslandHopping {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int z = in.nextInt();
		for (int q = 0; q < z; q++) {
			// Input
			int N = in.nextInt();
			double[] xCoords = new double[N];
			double[] yCoords = new double[N];

			// Get island coords
			for (int i = 0; i < N; i++) {
				xCoords[i] = in.nextDouble();
				yCoords[i] = in.nextDouble();
			}

			// Prim's
			double[] distances = new double[N];
			for (int i = 1; i < N; i++) {
				distances[i] = Integer.MAX_VALUE;
			}
			HashSet<Integer> visited = new HashSet<Integer>();
			int current = 0;
			int count = 1;
			double total = 0;
			while (count < N) {
				// Visit this island
				visited.add(current);

				// Try to update distances with all the new neighbors
				for (int i = 0; i < N; i++) {
					if (i == current) {
						continue;
					}
					double newDistance = (xCoords[current]-xCoords[i])*(xCoords[current]-xCoords[i]) + (yCoords[current]-yCoords[i])*(yCoords[current]-yCoords[i]);
					
					// Replace the old distance with the shorter one
					if (newDistance < distances[i]) {
						distances[i] = newDistance;
					}
				}

				// Find the next island
				int nextIsland = 0;
				double bestDistance = Integer.MAX_VALUE;
				for (int i = 0; i < N; i++) {
					if (visited.contains(i)) {
						continue;
					}

					if (distances[i] < bestDistance) {
						bestDistance = distances[i];
						nextIsland = i;
					}
				}
				// Update current
				count++;
				total += Math.sqrt(bestDistance);
				current = nextIsland;
				//System.out.println(nextIsland);
			}
			System.out.println(total);
		}
	}
}