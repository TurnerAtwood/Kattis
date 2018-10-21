/*	Turner Atwood
 *	10/21/18
 *	Movie Collection [5.7] (https://open.kattis.com/problems/moviecollection)
 *	Memoized Linked List ... ?[DP]?
 */

import java.util.Scanner;
import java.util.ArrayList;
import java.lang.StringBuilder;

/*
	The movies are stored in a linked list (the front is the top of the stack).
	Every time a movie is selected a few things happen:
		1) The location of every movie is stored in a memo array
		2) The quickAccess nodes are updated to stay in the same spots

	Without any memoization this algorithm would be O(n*m)
	With the quickAccess nodes to prevent a full linear scan each search,
		this algorithm performs much, much better.
	A frequency of 1 or n would result in the same behavior as the naive approach.
*/

class MovieCollection {

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int caseNum = in.nextInt();
		for(int z = 0; z < caseNum; z++) {
			int movieNum = in.nextInt();
			int queuryNum = in.nextInt();
			
			// Frequency could be optimized dynamically for better performance
			int freq = 150;

			// Create a fresh linkedlist
			LinkedList movies = new LinkedList(movieNum, freq);

			//Process output and print results
			int look;
			StringBuilder result = new StringBuilder("");
			for (int i = 0; i < queuryNum; i++) {
				look = in.nextInt()-1;
				int spot = movies.select(look);
				result.append(spot+ " ");
			}
			System.out.println(result);	

			//Supplementary Prints (ALL INFO IN LINKEDLIST)
			//System.out.println("RESLT: " + result);	
			//System.out.println("LLIST: " + movies.dumpList());	
			//System.out.println("LSEEN: " + movies.dumpLastSeen());
			//System.out.println("QKACC: " + movies.dumpQuickAccess());
			//System.out.println("----------------------");

		}
	}

	static class LinkedList {

		//Standard LinkedList Items
		Node first;
		Node last;
		int size;

		//Memoization Items
		ArrayList<Integer> lastSeen;
		ArrayList<Node> quickAccess;
		int frequency;

		// Constructor calls buildList to reduce clutter
		LinkedList(int size, int freq) {
			this.size = size;
			frequency = freq;
			quickAccess = new ArrayList<Node>();
			lastSeen = new ArrayList<Integer>();
			buildList();
		}

		// initializes all field variables to starting values
		void buildList() {
			// The first Item is special
			Node newNode = new Node(0);
			first = newNode;
			last = first;
			lastSeen.add(0);
			quickAccess.add(newNode);

			// Building elements for items 1 to (n-1)
			for (int i = 1; i < size; i++) {
				newNode = new Node(i);
				append(newNode);

				//Memoization initialization
				lastSeen.add(i);
				if (i%frequency == 0) {
					quickAccess.add(newNode);
				}
			}
		}

		// Finds the movie and updates the entire LinkedList accordingly
		int select(int selected) {
			// Weird things happen when a node is both the front and end
			if (size == 1) {
				return 0;
			}

			// Find out how far in the linkedlist you can start
			//		This step shows how quickIndex allows faster finds
			//		without it, current = first & count = 0 always.
			int quickIndex = getQuickIndex(selected);
			Node current = quickAccess.get(quickIndex);
			int count = quickIndex*frequency;

			// Linear scan over part of the LinkedList to find the movie wanted
			while (current.value != selected) {				
				
				// Update quickAccesses as you pass them 
				//	  Can't do the first one since it has no previous Node yet 
				if (count%frequency == 0 && count != 0) {
					quickUpdate(count/frequency);
				}
				count++;

				// Update the lastSeen array for as many nodes as possible
				lastSeen.set(current.value, count);
				current = current.next;				
			}

			// Update memoization for selected Node	(still can't update first)
			lastSeen.set(selected, 0);
			if (count%frequency == 0 && count != 0) {
				quickUpdate(count/frequency);
			}

			// Move slected to the front
			remove(current);
			push(current);

			// Update all previous quickAccess elements
			//	 Make sure we will update the first quickAccess node if needed
			if (quickIndex == 0 && count != 0) {
				quickIndex++;
			}
			adjustQuickAccess(quickIndex);
			return count;
		}

		// Standard LinkedList Remove
		void remove(Node selected) {
			if (first.value == selected.value) {
				Node newFirst = selected.next;
				newFirst.previous = null;
				first = newFirst;
			}
			else if (last.value == selected.value){
				Node newLast = selected.previous;
				newLast.next = null;
				last = newLast;
			}
			else {
				Node beforeNode = selected.previous;
				Node  afterNode = selected.next;
				beforeNode.next = afterNode;
				afterNode.previous = beforeNode;
			}

			// Ensure no dangling pointers occur
			selected.previous = null;	
			selected.next = null;
		}

		// Push a Node to the front
		void push(Node newNode) {
			newNode.previous = null;
			Node oldFirst = first;
			oldFirst.previous = newNode;
			newNode.next = oldFirst;
			first = newNode;
		}

		// Append a Node to the end (only for building)
		void append(Node newNode) {
			Node oldLast = last;
			oldLast.next = newNode;
			newNode.previous = oldLast;
			last = newNode;
		}

		// Standard LinkedList Insert (Never Used)
		void insert(Node beforeNode, Node newNode) {
			if (last.value == beforeNode.value) {
				append(newNode);
			}
			else {
				Node afterNode = beforeNode.next;
				beforeNode.next = newNode;
				newNode.previous = beforeNode;
				afterNode.previous = newNode;
				newNode.next = afterNode;
			}
		}

		//     QuickAccess Helpers     //

		// Finds the closest quickAccessNode based on the lastSeen
		int getQuickIndex(int selected) {
			int ls = lastSeen.get(selected);
			int index = ls/frequency;
			return index;
		}

		// Adjusts quickAccess Nodes skipped over in the selection
		//	  Each must be pushed back one space to maintain position
		void adjustQuickAccess(int quickIndex) {
			for (int i = 0; i < quickIndex; i++) {
				quickUpdate(i);
			}
		}

		// Pushes a single quickAccess Node back an element
		void quickUpdate(int quickIndex) {
			Node oldNode = quickAccess.get(quickIndex);
			quickAccess.set(quickIndex, oldNode.previous);
		}

		//     Printing Methods     //

		// Spits out the elements of the LinkedList in order
		String dumpList() {
			Node current = first;
			StringBuilder sb = new StringBuilder();
			while (current != null) {
				sb.append(current.value + " ");
				current = current.next;
			}
			return sb.toString();
		}

		// Spits where each Node was last seen
		String dumpLastSeen() {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < size; i++) {
				sb.append(lastSeen.get(i) + " ");
			}
			return sb.toString();
		}

		// Spits out the quickAccess elements
		String dumpQuickAccess() {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < quickAccess.size(); i++) {
				sb.append(quickAccess.get(i).value + " ");
			}
			return sb.toString();
		}
	}

	// Standard Node for a LinkedList
	static class Node {
		int value;
		Node next;
		Node previous;

		Node(int val) {
			value = val;
			next = null;
			previous = null;
		}
	}
}

/*
Vanilla, operationalLinkedList
static class LinkedList {

		Node first;
		Node last;

		LinkedList(Node initial) {
			first = initial;
			last = initial;
		}

		int select(int selected) {
			Node current = first;
			int count = 0;
			while (current.value != selected) {
				current = current.next;
				count++;
			}
			remove(current);
			push(current);
			return count;
		}

		Node remove(Node selected) {
			if (first.value == selected.value) {
				//cout << "FIRST\n";
				Node newFirst = selected.next;
				newFirst.previous = null;
				first = newFirst;
			}
			else if (last.value == selected.value){
				//cout << "LAST\n";
				Node newLast = selected.previous;
				newLast.next = null;
				last = newLast;
			}
			else {
				//cout << "MIDDLE\n";
				selected.previous.next = selected.next;
			}
			selected.previous = null;	
			selected.next = null;
			return selected;
		}

		void push(Node newNode) {
			Node oldFirst = first;
			oldFirst.previous = newNode;
			newNode.next = oldFirst;
			first = newNode;
		}

		void append(Node newNode) {
			Node oldLast = last;
			oldLast.next = newNode;
			newNode.previous = oldLast;
			last = newNode;
		}

		void insert(Node beforeNode, Node newNode) {
			if (last.value == beforeNode.value) {
				append(newNode);
			}
			else {
				Node afterNode = beforeNode.next;
				beforeNode.next = newNode;
				newNode.previous = beforeNode;
				afterNode.previous = newNode;
				newNode.next = afterNode;
			}
		}

		String dump() {
			Node current = first;

			StringBuilder sb = new StringBuilder();
			while (current != null) {
				sb.append(current.value + " ");
				current = current.next;
			}

			return sb.toString();
		}
	}
*/

/*
LinkedList with lastSeen working
static class LinkedList {

		Node first;
		Node last;
		int size;
		ArrayList<Integer> lastSeen;
		ArrayList<Node> quickAccess;
		int frequency;

		LinkedList(int size, int freq) {
			this.size = size;
			frequency = freq;
			quickAccess = new ArrayList<Node>();
			lastSeen = new ArrayList<Integer>();
			buildList();
		}

		void buildList() {
			Node newNode = new Node(0);
			first = newNode;
			last = first;
			lastSeen.add(0);
			for (int i = 1; i < size; i++) {
				newNode = new Node(i);
				append(newNode);
				lastSeen.add(i);
			}
		}

		int select(int selected) {
			Node current = first;
			int count = 0;
			while (current.value != selected) {				
				count++;
				lastSeen.set(current.value, count);
				current = current.next;
				if (current == null) {
					System.out.println("\nBAD: " + dumpList());
				}
			}
			lastSeen.set(selected, 0);
			remove(current);
			push(current);
			return count;
		}

		void remove(Node selected) {
			if (first.value == selected.value) {
				Node newFirst = selected.next;
				newFirst.previous = null;
				first = newFirst;
			}
			else if (last.value == selected.value){
				Node newLast = selected.previous;
				newLast.next = null;
				last = newLast;
			}
			else {
				Node beforeNode = selected.previous;
				Node  afterNode = selected.next;
				beforeNode.next = afterNode;
				afterNode.previous = beforeNode;
			}
			selected.previous = null;	
			selected.next = null;
		}

		void push(Node newNode) {
			newNode.previous = null;
			Node oldFirst = first;
			oldFirst.previous = newNode;
			newNode.next = oldFirst;
			first = newNode;
		}

		void append(Node newNode) {
			Node oldLast = last;
			oldLast.next = newNode;
			newNode.previous = oldLast;
			last = newNode;
		}

		void insert(Node beforeNode, Node newNode) {
			if (last.value == beforeNode.value) {
				append(newNode);
			}
			else {
				Node afterNode = beforeNode.next;
				beforeNode.next = newNode;
				newNode.previous = beforeNode;
				afterNode.previous = newNode;
				newNode.next = afterNode;
			}
		}

		String dumpList() {
			Node current = first;
			StringBuilder sb = new StringBuilder();
			while (current != null) {
				sb.append(current.value + " ");
				current = current.next;
			}
			return sb.toString();
		}

		String dumpLastSeen() {
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < size; i++) {
				sb.append(lastSeen.get(i) + " ");
			}
			return sb.toString();
		}
	}
*/