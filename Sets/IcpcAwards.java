/*	Turner Atwood
 *	10/15/19
 *	ICPC Awards [1.4] https://open.kattis.com/problems/icpcawards
 *	Trivial Set Example
 */

import java.util.Scanner;
import java.util.HashSet;

public class IcpcAwards {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int n = Integer.parseInt(in.nextLine());
		int place = 0;
		HashSet<String> schools = new HashSet<String>();
		String[] results = new String[12];
		String[] placing;
		for (int i = 0; i < n; i++) {
			placing = in.nextLine().split(" ");
			
			if (schools.contains(placing[0])) {
				continue;
			}
			
			schools.add(placing[0]);
			results[place] = placing[0] + " " + placing[1];
			place++;
			
			if (schools.size() == 12) {
				break;
			}

		} 

		for (int i = 0; i < 12; i++) {
			System.out.println(results[i]);
		}
	}
}