/*  Turner Atwood
 *  10/15/16
 *  Kastenlauf [3.7]: (https://open.kattis.com/problems/kastenlauf)
 */ 

import java.util.*;

public class Kastenlauf {
  static ArrayList<Node> map;
  static int num;
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int abc = in.nextInt();
    for (int i = 0; i < abc; i++) {
      num = in.nextInt() + 2;
      map = new ArrayList<Node>();
      for(int j = 0; j < num; j++) {
        Point place = new Point(in.nextInt(), in.nextInt());
        map.add(new Node(place));
      }
      Node last = map.get(num - 1);
      for (int j = 0; j < num; j++) {
        Node look = map.get(j);
        for (int k = 0; k < num; k++) {
          Node lack = map.get(k);
          int dist = look.getPoint().distance(lack.getPoint());
          if (dist > 0 && dist <= 1000) {
            look.neighbors.add(lack);
          }
        }
      }
      if (findEnd(map.get(0))) {
        System.out.println("happy");
      }
      else {
        System.out.println("sad");
      }
    }
  }
    public static boolean findEnd(Node a) {
      a.visited = true;
      if (a.equals(map.get(num-1))) {
        return true;
      }
      for (Node neigh : a.neighbors) {
        if (!neigh.visited) {
          if (findEnd(neigh)) {
            return true;
          }
        }

      }
      return false;
    }

  private static class Point {
     int X;
     int Y;

    public Point() {
      X = 0;
      Y = 0;
    }

    public Point(int a, int b) {
      X = a;
      Y = b;
    }

    public int getX() {
      return X;
    }

    public int getY() {
      return Y;
    }

    public int distance(Point that) {
      return (Math.abs(this.getX() - that.getX()) + Math.abs(this.getY() - that.getY()));
    }
  }

  private static class Node {
    List<Node> neighbors = new ArrayList<>();
    Point spot = new Point();
    boolean visited = false;

    public Node(Point p) {
      spot = p;
    }

    public Point getPoint() {
      return spot;
    }
  }
}
