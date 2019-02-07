/*
	Turner Atwood
	2/7/19
	Last Factorial Digit [1.2]: (https://open.kattis.com/problems/lastfactorialdigit)
	Trivial
*/

import java.util.*;

class LastFactorialDigit {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);

		int T = in.nextInt();
		for(int i = 0; i < T; i++) {
			int N = in.nextInt();
			System.out.println(factDig(N));
		}
	}

	static int factDig(int N) {
		int res = 1;
		for (int i = 1; i <= N; i++) {
			res = (res*i)%10;
		}
		return res;
	}
}