/*  Turner Atwood
 *  2/16/17
 *  Gears [4.4]: (https://open.kattis.com/problems/gears2)
 */ 

import java.util.*;
import java.lang.Math;

class Gears {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int num = in.nextInt();
    ArrayList<Node> gearSystem = new ArrayList<Node>();
    for (int i = 0; i < num; i++) {
      Node look = new Node(in.nextInt(), in.nextInt(), in.nextInt());
      if (i == 0) {
        look.setDirection(1);
      }
      for (Node other : gearSystem) {
        if (look.isTouching(other)) {
          look.neighbors.add(other);
          other.neighbors.add(look);
        }
      }
      gearSystem.add(look);
    }
    //TEST print
    /*System.out.println("BEFORE: ");
    for (int i = 0; i < num; i++) {
      gearSystem.get(i).print(0);
    }*/
    //Do a DFS to get the rotations right
    Node last = gearSystem.get(num-1);
    Node first = gearSystem.get(0);
    LinkedList<Node> queue = new LinkedList<Node>();
    queue.addFirst(first);
    while (!queue.isEmpty()) {
      Node look = queue.remove();
      //look.print(0);
      look.visited = true;
      for (Node neigh : look.neighbors) {
        if (!neigh.visited) {
          queue.addLast(neigh);
          if (!neigh.setDirection(look.direction * -1)) {
            System.out.println("-1");
            return;
          }
        }
      }
    }
    //TEST print
    /*System.out.println("AFTER: ");
    for (int i = 0; i < num; i++) {
      gearSystem.get(i).print(0);
    }*/
    //If direction of last gear is 0 it is not connected to source
    if (last.direction == 0) {
      System.out.println("0");
      return;
    }
    int gcd = gcd(first, last);
    System.out.println(last.R/gcd + " " + first.R/gcd * last.direction);
    return;
  }

  //GCD of 2 numbers
  public static int gcd(Node A, Node B) {
    int a = A.R;
    int b = B.R;
    int tmp;
    if (b > a) {
      tmp = b;
      b = a;
      a = tmp;
    }
    while (b > 0) {
      tmp = a%b;
      a = b;
      b = tmp;
    }
    return a;
  }

  static class Node {
    public int X;
    public int Y;
    public int R;
    public ArrayList<Node> neighbors;
    public boolean visited;
    public int direction;

    public Node(int x, int y, int r) {
      X = x;
      Y = y;
      R = r;
      neighbors = new ArrayList<Node>();
      visited = false;
      direction = 0;
    }

    //ROunding problem??!
    public boolean isTouching(Node other) {
      int dist = (X - other.X)*(X - other.X) + (Y - other.Y)*(Y - other.Y);
      if (dist == (R + other.R)*(R + other.R)) {
        return true;
      }
      return false;
    }

    //Returns false if the gear is spun 2 different directions
    public boolean setDirection(int dir) {
      if (direction == 0) {
        direction = dir;
        return true;
      }
      if (direction != dir) {
        return false;
      }
      return true;
    }

    //Makes printing easier
    public void print(int a) {
      System.out.println("[(" + X + ", " + Y + "), " + R + ", " + direction + "]");
      if (a == 0) {
        for (int i = 0; i < neighbors.size(); i++) {
          System.out.print("   ");
          neighbors.get(i).print(1);
        }
      }
    }
  }
}
