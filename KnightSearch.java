/*	Turner Atwood
 *	10/31/18
 *	Knight Search [3.1] (https://open.kattis.com/problems/knightsearch)
 *	Standard DFS (Started from multiple locations)
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.ArrayList;
import java.util.LinkedList;

class KnightSearch {
	// These are global for the neighbor functions
	static int N;
	static String board;
	static String search = "ICPCASIASG";

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = br.readLine();

		// Begin a DFS from every instance of "I"
		LinkedList<Node> stack = new LinkedList<Node>();
		for (int i = 0; i < N*N; i++) {
			char check = board.charAt(i);
			if (check == 'I') {
				stack.push(new Node(i, 0));
			}
		}

		// Run a DFS from all start points
		boolean found = false;
		while (!stack.isEmpty()) {
			Node current = stack.pop();
			int nextIndex = current.findIndex+1;
			
			// Exit condition
			if (nextIndex == search.length()) {
				found = true;
				break;
			}

			char nextLook = search.charAt(nextIndex);
			ArrayList<Integer> neighbors = getNeighbors(current.location, nextLook);
			for (Integer neigh : neighbors) {
				stack.push(new Node(neigh, nextIndex));
			}
		}

		// Output
		String out = "NO";
		if (found) {
			out = "YES";
		}
		System.out.println(out);
	}

	// Find the neighbors that have the desired character
	static ArrayList<Integer> getNeighbors(int current, char look) {
		ArrayList<Integer> neighbors = new ArrayList<Integer>();
		for (int i = -2; i < 3; i++) {
			for (int j = -2; j < 3; j++) {
				int possNeigh = current + i*N + j;
				if (isNeighbor(current, possNeigh)) {
					if (board.charAt(possNeigh) == look) {
						neighbors.add(possNeigh);
					}
				}
			}
		}
		return neighbors;
	}

	// See if spot2 is a knight move away from spot1
	static boolean isNeighbor(int spot1, int spot2) {
		// Make sure the spots are on the board
		if (spot1 < 0 || spot1 >= N*N || spot2 < 0 || spot2 >= N*N) {
			return false;
		}

		int b = spot1/N;
		int a = spot1%N;
		int d = spot2/N;
		int c = spot2%N;
		if (((a-c)*(a-c)+(b-d)*(b-d)) == 5) {
			return true;
		}
		return false;
	}

	// Just used to package info for the DFS
	static class Node {
		int location;
		int findIndex;

		Node(int l, int f) {
			location = l;
			findIndex = f;
		}

	}
}