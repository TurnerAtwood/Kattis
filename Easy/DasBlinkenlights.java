/*	Turner Atwood
 *	2/18/19
 *	Das Blinkenlights [1.9]: https://open.kattis.com/problems/dasblinkenlights
 *	Simple LCM calculation
 */

import java.util.*;

class DasBlinkenlights {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int b = in.nextInt();
		int N = in.nextInt();
		if (lcm(a,b) <= N) {
			System.out.println("yes");
		}
		else {
			System.out.println("no");
		}
	}

	// Simple LCM calculator
	static int lcm(int a, int b) {
		HashSet<Integer> aSeen = new HashSet<Integer>();
		HashSet<Integer> bSeen = new HashSet<Integer>();
		if (a == b) {
			return a;
		}
		int lcm = 1;
		int factor = 1;
		while (lcm == 1) {
			int aNew = factor * a;
			int bNew = factor * b;
			if (bSeen.contains(aNew)) {
				lcm = aNew;
			}
			else if (aSeen.contains(bNew)) {
				lcm = bNew;
			}
			aSeen.add(aNew); 
			bSeen.add(bNew); 
			factor += 1;
		}
		return lcm;
	}
}