/*	Turner Atwood
 *	10/22/18
 *	Elevator Trouble [3.7] (https://open.kattis.com/problems/elevatortrouble)
 *	BFS - start at given floor and try to go up and down floors
 */

import java.util.Scanner;
import java.util.HashSet;
import java.util.LinkedList;


class ElevatorTrouble {
	
	static int MAX_VAL = 10000000;

	public static void main(String args[]) {
		// Only one line of input, so Scanner is fine
		Scanner in = new Scanner(System.in);
		int floorNum = in.nextInt();
		int start = in.nextInt()-1;
		int goal = in.nextInt()-1;
		int up = in.nextInt();
		int down = in.nextInt();
		
		// Initialize the array to search over
		boolean[] visited = new boolean[floorNum];
		int[] minDist = new int[floorNum];
		for (int i = 0; i < floorNum; i++) {
			minDist[i] = MAX_VAL;
			visited[i] = false;
		}
		minDist[start]= 0;

		// Standard BFS
		LinkedList<Integer> queue = new LinkedList<Integer>();
		queue.addLast(start);
		while (!queue.isEmpty()) {
			int current = queue.removeFirst();
			if (current == goal) {
				break;
			}

			// Try to go up
			int tryUp = current+up;
			if (tryUp < floorNum && minDist[current]+1 < minDist[tryUp]) {
				queue.addLast(tryUp);
				minDist[tryUp] = minDist[current]+1;
			}

			// Try to go down
			int tryDown = current-down;
			if (tryDown >= 0 && minDist[current]+1 < minDist[tryDown]) {
				queue.addLast(tryDown);
				minDist[tryDown] = minDist[current]+1;
			}
		}

		// Output
		int minGoal = minDist[goal];
		if (minGoal == MAX_VAL) {
			System.out.println("use the stairs");
		}
		else {
			System.out.println(minGoal);
		}
	}
}