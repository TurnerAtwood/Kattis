/*	Turner Atwood
 *	2/19/17
 *	Zamka [1.3] (https://open.kattis.com/problems/zamka)
 *
 */

import java.util.*;

class Zamka {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int L = in.nextInt();
    int D = in.nextInt();
    int X = in.nextInt();
    
    // Find minimal number
    for (int i = L; i <= D; i++) {
      if (sumD(i) == X) {
        System.out.println(i);
        i = D;
      }
    }

    // Find maximal number
    for (int i = D; i >= L; i--) {
      if (sumD(i) == X) {
        System.out.println(i);
        i = L;
      }
    }
  }

  // Calculates the sum of a numbers digits
  static int sumD(int a) {
    int ret = 0;
    while (a > 0) {
      ret += a%10;
      a /= 10;
    }
    return ret;
  }
}
