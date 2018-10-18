/*	Turner Atwood
 *	10/17/18
 *	Crane [6.3] (https://open.kattis.com/problems/crane2)
 *	Rewritten in java,python was too slow.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.lang.StringBuilder;

class Crane {
	// Better than passing them around in every parameter
	
	static int size;
	// crates[i] is the crate at spot i
	// crateisAt[i] is the location of crate i in crates
	static int[] crates;
	static int[] crateisAt;
	static ArrayList<String> moves;

	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cases = Integer.parseInt(br.readLine());
		for (int z = 0; z < cases; z++) {

			// Set up a new test case
			size = Integer.parseInt(br.readLine());
			crates = new int[size];
			crateisAt = new int[size];
			moves = new ArrayList<String>();

			// Grab all crate info and save it off
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < size; i++) {
				int crane = Integer.parseInt(st.nextToken())-1;
				crates[i] = crane;
				crateisAt[crane] = i;
			}
			
			// Move every crate to its final position
			for (int i = 0; i < size; i++) {
				movetoSpot(i);
			}

			// Print all of the moves
			System.out.println(moves.size());
			StringBuilder result = new StringBuilder();
			for (String move : moves) {
				System.out.println(move);
			}
		}
	}

	// Move the selected crate to its final position
	static void movetoSpot(int crate) {
		while (crates[crate] != crate) {
			int index = crateisAt[crate];
			int dist = index - crate+1;
			String move;

			// Try and move directly to the final spot
			int farIndex = index+dist-2;
			if (farIndex < size) {
				swap(crate, farIndex);
				move = (crate+1) + " " + (farIndex+1);
			}

			// Move one to the left
			else if (dist%2 != 0) {
				swap(index-1, index);
				move = index + " " + (index + 1);
			}
			// Move halfway to the final spot
			else {
				swap(crate, index);
				move = (crate+1) + " " + (index + 1);
			}

			//Store each move made to print later
			moves.add(move);
		}
	}

	// Perform a swap over the indicated interval
	// Order doesn't change between the two halves
	static void swap(int start, int stop) {
		int dist = stop - start + 1;
		// Can't swap an odd interval
		if (dist%2 != 0) {
			System.out.println("ODD INTERVAL");
			return;
		}

		// Make the swap over the interval
		dist /= 2;
		for(int i = start; i < start + dist; i++) {
			int oppIndex = i + dist;
			int crate1 = crates[i];
			int crate2 = crates[oppIndex];

			crates[i] = crate2;
			crates[oppIndex] = crate1;

			crateisAt[crate1] = oppIndex;
			crateisAt[crate2] = i;
		}

	}
}