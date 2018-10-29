/*	Turner Atwood
 *	10/29/18
 *	Jolly Jumpers [3.2] (https://open.kattis.com/problems/jollyjumpers)
 *	See if consecutive differences in a set are {1,2, ... , n-1}
 */

import java.util.Scanner;
import java.util.HashSet;
import java.lang.Math;

class JollyJumpers {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		while (in.hasNext()) {
			String line = in.nextLine();
			String[] numbers = line.split(" ");
			int size = Integer.parseInt(numbers[0]);

			// Build the expected set {1,2, ... ,size-1}
			HashSet<Integer> expected = new HashSet<Integer>();
			for (int i = 1; i < size; i++) {
				expected.add(i);
			}

			// Try to remove the difference of consective numbers
			//	 from the expected set
			for (int i = 1; i < size; i++) {
				int num1 = Integer.parseInt(numbers[i]);
				int num2 = Integer.parseInt(numbers[i+1]);
				int diff = Math.abs(num1-num2);
				expected.remove(diff);
			}

			// Jolly if you removed every expected number
			if (expected.isEmpty() || size == 1) {
				System.out.println("Jolly");
			}
			else {
				System.out.println("Not jolly");
			}
		}
	}
}