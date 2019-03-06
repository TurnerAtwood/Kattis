/*  Turner Atwood
 *  2/15/17
 *  Dyslectionary [3.4]: (https://open.kattis.com/problems/dyslectionary)
 *  Simple Comparator implementation (old)
 */ 

import java.util.*;

class Dyslectionary {
  
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    String look = "begin";
    while (in.hasNext()) {
        List<String> words = new ArrayList<String>();
        int max  = 0;
        look = in.nextLine();
        while (look.length() != 0) {
          int comp = look.length();
          if (comp > max) {
            max = comp;
          }
          words.add(look);
          if (in.hasNext()) {
            look = in.nextLine();
          }
          else {
            look = "";
          }
        }

      Collections.sort(words, new Com());
        print(words, max);
        if (in.hasNext()) {
          System.out.println();
        }
    }
  }


    static void print(List<String> lst, int max){
      for (int i = 0; i < lst.size(); i++) {
        String look = lst.get(i);
        System.out.println(zero(max - look.length()) + look);
      }
    }

    // Generates a string of all " " of length a (for prepending)
    public static String zero(int a) {
      String ret = "";
      for (int i = 0; i < a; i++) {
        ret += " ";
      }
      return ret;
    }

    // Compare strings based on their reversal
    static class Com implements Comparator<String> {
      public int compare(String a, String b) {
        if (a.equals(b)) {
          return 0;
        }
        StringBuilder as = new StringBuilder(a.toLowerCase());
        StringBuilder bs = new StringBuilder(b.toLowerCase());
        as.reverse();
        bs.reverse();
        return (as.toString().compareTo(bs.toString()));
      }
    }
  }