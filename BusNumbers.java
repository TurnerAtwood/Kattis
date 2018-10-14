/*  Turner Atwood
 *  10/05/16
 *  Bus Numbers [2.5] (https://open.kattis.com/problems/busnumbers)
 */

import java.util.*;

public class BusNumbers {
  public static void main (String args[]) {
    Scanner in = new Scanner(System.in);
    int num = Integer.parseInt(in.nextLine());
    String[] buss = in.nextLine().split(" ");
    int[] busses = new int[num];
    for (int i = 0; i < num; i++) {
      busses[i] = Integer.parseInt(buss[i]);
    }
    Arrays.sort(busses);
    int count = 1;
    String print = "";
    int look = busses[0];
    int start = look;
    int last = look;
    if (num == 1) {
      print += look;
    }
    for (int i = 1; i < num; i++) {
      look = busses[i];
      if ( look == start + count) {
        count++;
      }
      else {
        if (start != last) {
          if (count > 2) {
            print += start + "-" + last + " ";
          }
          else {
            print += start + " " + last + " ";
          }
        }
        else {
          print += start + " ";
        }
        count = 1;
        start = look;
      }
      if (i == num - 1) {
        if (start != look) {
          if (count > 2) {
            print += start + "-" + look;
          }
          else {
            print += start + " " + look + " ";
          }
        }
        else {
          print += start;
        }
      }
      last = look;
    }
    System.out.println(print);
  }
}
