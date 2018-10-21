/*	Turner Atwood
 *	10/21/12
 *	10 Kinds of People [5.5] (https://open.kattis.com/problems/10kindsofpeople)
 *	UnionFind
 */

import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.StringTokenizer;
import java.util.HashSet;
import java.lang.StringBuilder;

/*	Standard unionfind over a 2D array
 *	Python was too slow
 */

class TenKindsofPeople {
	static final int[][] directions = {{-1,0},{0,-1},{0,1},{1,0}};
	// Making these global makes life easier for all the array operations
	static int height;
	static int width;
	static int size;
	static int[] board;
	static int[] parent;

	public static void main(String args[]) throws IOException{
		// Lots of variabe initialization
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());	
		height = Integer.parseInt(st.nextToken());
		width = Integer.parseInt(st.nextToken());
		size = height*width;
		board = new int[size];
		parent = new int[size];
		
		// Fill the board and parent arrays
		for (int i = 0; i < height; i++) {
			String line = br.readLine();
			for (int j = 0; j < width; j++) {
				int index = i*width+j;
				board[index] = line.charAt(j)-48;
				parent[index] = index;
			}
		}

		// Union all neighbors in board
		buildUnionFind();

		// Perform queries, print results
		StringBuilder sb = new StringBuilder();
		int queryNum = Integer.parseInt(br.readLine());
		for (int i = 0; i < queryNum; i++) {
			st = new StringTokenizer(br.readLine());	
			int h1 = Integer.parseInt(st.nextToken())-1;
			int w1 = Integer.parseInt(st.nextToken())-1;
			int h2 = Integer.parseInt(st.nextToken())-1;
			int w2 = Integer.parseInt(st.nextToken())-1;
			int index1 = h1*width + w1;
			int index2 = h2*width + w2;
			sb.append(query(index1, index2) + "\n");
		}
		System.out.print(sb);

		// Supplementary Prints
		//printBoard();
		//System.out.println("-------------");
		//printParent();
	}
	
	// UnionFind Operations //

	// Staandard find with path compression
	static int find(int index) {
		if (parent[index] == index) {
			return index;
		}
		parent[index] = find(parent[index]);
		return parent[index];
	}

	// Standard union
	static void union(int index1, int index2) {
		int parent1 = find(index1);
		int parent2 = find(index2);

		if (parent2 < parent1) {
			parent[parent1] = parent2;
		}
		else {
			parent[parent2] = parent1;
		}
	}

	// Given an index, union all of its neighbors with the same value
	static void tryUnion(int baseIndex) {
		HashSet<Integer> neighbors = getNeighbors(baseIndex);
		for (int neighbor : neighbors) {
			if (board[baseIndex] == board[neighbor]) {
				union(baseIndex, neighbor);
			}
		}
	}

	// Perform tryUnion on all elements of board
	static void buildUnionFind() {
		for (int i = 0; i < size; i++) {
			tryUnion(i);
		}
	}

	// Generate output for a query on two indices
	static String query(int index1, int index2) {
		boolean joined = find(index1) == find(index2);
		if (!joined) {
			return "neither";
		}
		else if (board[index1] == 0) {
			return "binary";
		}
		else {
			return "decimal";
		}
	}

	// Neighbor Operations //

	// Check to see if checkindex is next to baseindex
	static int checkAdjacent(int baseIndex, int checkIndex) {
		// Make sure the trial index is in bounds
		if (checkIndex < 0 || checkIndex >= size) {
			return -1;
		}
		int h1 = baseIndex/width;
		int w1 = baseIndex%width;
		int h2 = checkIndex/width;
		int w2 = checkIndex%width;
		// Make sure they are not wrapped around to a new line
		if (h1 != h2 && w1 != w2) {
			return -1;
		}
		return checkIndex;
	}

	// Returns all viable neighbors of an index
	static HashSet<Integer> getNeighbors(int baseIndex) {
		HashSet<Integer> neighbors = new HashSet<Integer>();
		for (int[] direction : directions) {
			int offset = (direction[0]*width + direction[1]);
			int checkIndex = baseIndex + offset;
			checkIndex = checkAdjacent(baseIndex, checkIndex);
			neighbors.add(checkIndex);
		}
		neighbors.remove(-1);
		return neighbors;
	}
	
	//     Printing Methods     //
	
	// Print the board row by row
	static void printBoard() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				System.out.print(board[i*width+j]);	
			}
			System.out.println();
		}
	}

	// Print the parent array row by row
	static void printParent() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				int val = find(i*width+j);
				System.out.printf("%03d ", val);	
			}
			System.out.println();
		}
	}
}