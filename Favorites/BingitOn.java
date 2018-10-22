
/*	Turner Atwood
 *	10/22/18
 *	Bing it On [4.3] (https://open.kattis.com/problems/bing)
 *	Prefix Tree - Python was too slow
 */

import java.util.HashMap;
import java.util.ArrayList;
import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.StringTokenizer;
import java.lang.StringBuilder;

class BingitOn {

	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		PrefixTree pTree = new PrefixTree();

		//StringBuilder to reduce the time to print/append lots of strings
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < num; i++) {
			String line = br.readLine();
			sb.append(pTree.isPrefix(line)+"\n");
		}

		System.out.print(sb);
	}

	static class PrefixTree {
		Node root;

		PrefixTree() {
			root = new Node(' ');
		}

		// Add a line of nodes based on the given string
		//	 starting at the given node
		void addToTree(String letters, Node current_parent) {
			for (int i = 0; i < letters.length(); i++) {
				char new_letter = letters.charAt(i);
				Node new_Node = new Node(new_letter);
				current_parent.children.put(new_letter, new_Node);
				current_parent = new_Node;
			}
		}

		// Returns how many previous strings use this string as a prefix
		//	Also adds to the tree if a string is not a prefix and updates counters
		int isPrefix(String letters) {
			Node current_node = root;
			for (int i = 0; i < letters.length(); i++) {
				char match_letter = letters.charAt(i);
				Node next_node = current_node.find(match_letter);
				
				// Not a prefix
				if (next_node == null) {
					addToTree(letters.substring(i), current_node);
					return 0;
				}
				next_node.count++;
				current_node = next_node;
			}
			return current_node.count;
		}
	}

	// NODE SUBCLASS
	static class Node {
		int count;
		char val;
		HashMap<Character,Node> children;

		Node(char in_val) {
			val = in_val;
			count = 0;
			children = new HashMap<Character,Node>();
		}

		// Find the value for the given character in children
		Node find(char match_letter) {
			if (children.containsKey(match_letter)) {
				return children.get(match_letter);
			}
			return null;
		}
	}
}