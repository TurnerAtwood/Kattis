/*	Turner Atwood
 *	9/4/19
 *	Quality-Adjusted Life-Year [1.3] https://open.kattis.com/problems/qaly
 *	Ad-hoc : Trivial
 */

import java.util.*;

public class Qaly {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();

		double total = 0;

		for (int i = 0; i < n; i++) {
			double left = in.nextDouble();
			double right = in.nextDouble();

			double mult = left * right;
			total += mult;
		}

		System.out.println(total);
	}
}