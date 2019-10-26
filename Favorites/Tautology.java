/*	Turner Atwood
 *	8/27/19
 *	Tautology [3.4] https://open.kattis.com/problems/tautology
 *	Brute Force every combination of variables -
 **	Use a tree to carry out the boolean logic
 **	There are easier ways to do this but
 **	this is a great example use of a tree
 */

import java.util.Scanner;

public class Tautology {

	static String WFF;
	static int[] values;

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		while (true) {
			WFF = in.nextLine();
			if (WFF.equals("0")) {
				break;
			}
			Node tree = buildTree();

			boolean tautology = true;
			// Try all 2^5 combos
			for (int i = 0; i < 32; i++) {
				values = intToBinaryArray(i);

				if (!executeTree(tree)) {
					tautology = false;
					break;
				}
			}

			if (tautology) {
				System.out.println("tautology");
			}
			else {
				System.out.println("not");
			}
		}
	}

	// Recursively build tree
	static Node buildTree() {
		Node current = new Node();
		char value = WFF.charAt(0);
		current.value = value;
		WFF = WFF.substring(1);

		if (!(value >= 'p' && value <= 't')) {
			current.operation = true;
			current.left = buildTree();
			if (value != 'N') {
				current.right = buildTree();
			}
		}

		return current;
	}

	static boolean executeTree(Node current) {
		if (!current.operation) {
			int value = values[current.value-'p'];
			if (value == 1) {
				return true;
			}
			else {
				return false;
			}
		}

		boolean left = executeTree(current.left);

		if (current.value == 'N') {
			return !left;
		}

		boolean right = executeTree(current.right);

		if (current.value == 'K') {
			return (left && right);
		}
		if (current.value == 'A') {
			return (left || right);
		}
		if (current.value == 'C') {
			return (!left || (left && right));
		}
		if (current.value == 'E') {
			return (left == right);
		}

		System.out.println("PROBLEM");
		return false;

	}

	public static class Node {
		boolean operation = false;
		char value;
		Node left;
		Node right;
	}

	static int[] intToBinaryArray(int a) {
		int len = 5;
		int[] result = new int[len];
		for (int i = 0; i < len; i++) {
			result[len-1-i] = a%2;
			a /= 2;
		}
		return result;
	}
}