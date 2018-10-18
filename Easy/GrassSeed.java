/*  Turner Atwood
 *  2/26/17
 *  Grass Seed Inc. [1.3]: (https://open.kattis.com/problems/grassseed)
 */ 

import java.util.*;

// Find areas of rectangles and multiply by a given cost
class GrassSeed {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    Double cost = in.nextDouble();
    int num = in.nextInt();
    Double tot = 0.0;
    for (int i = 0; i < num; i++) {
      tot += (in.nextDouble() * in.nextDouble()) * cost;
    }
    
    System.out.println(tot);
  }
}
