/*  Turner Atwood
 *  10/16/16
 *  Human Cannonball Run [3.4]: (https://open.kattis.com/problems/humancannonballrun)
 */ 

import java.util.*;

public class HumanCannonballRun {
  public static Node last;

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    ArrayList<Node> cannons = new ArrayList<Node>();
    cannons.add(new Node(in.nextDouble(), in.nextDouble()));
    cannons.add(new Node(in.nextDouble(), in.nextDouble()));
    last = cannons.get(1);
    int num = in.nextInt();
    for (int i = 0; i < num; i++) {
      cannons.add(1, new Node(in.nextDouble(), in.nextDouble()));
    }
    num += 2;
    for (int i = 0; i < num; i++) {
      Node look = cannons.get(i);
      for (int j = 0; j < num; j++) {
        if (i != j) {
          Node lack = cannons.get(j);
          cannons.get(i).neighbors.add(lack);
          double addTime = 0;
          if (i == 0) {
            addTime = look.distance(lack)/5;
          }
          else {
            addTime = 2 + Math.abs(look.distance(lack)-50)/5;
          }
          cannons.get(i).times.add(addTime);
        }
      }
    }
    System.out.println(dijkstra(cannons.get(0), last));

  }

  private static double dijkstra(Node a, Node b) {
    PriorityQueue<Node> pq = new PriorityQueue<>();
    a.time = 0;
    pq.add(a);
    while (!pq.isEmpty()) {
      Node c = pq.poll();
      c.visited = true;
      if (c == b) {
        return b.time;
      }
      for (int i = 0; i < c.neighbors.size(); i++) {
        Node d = c.neighbors.get(i);
        double thisTime = c.times.get(i);
        double newTime = c.time + thisTime;
        if (newTime < d.time) {
          pq.remove(d);
          d.time = newTime;
          pq.add(d);
        }
      }
    }
    return -1;
  }

  public static class Node implements Comparable<Node>{
    List<Node> neighbors = new ArrayList<Node>();
    List<Double> times = new ArrayList<Double>();
    public double X;
    public double Y;
    public double time;
    public boolean visited = false;

    public Node(double a, double b) {
      X = a;
      Y = b;
      time = Double.MAX_VALUE;
    }
    @SuppressWarnings("unchecked")
    public int compareTo(Node tht) {
      Node that = tht;
      double ret = this.time - that.time;
      if (ret < 0) {
        return -1;
      }
      if (ret > 0) {
        return 1;
      }
      return 0;
    }

    public double distance(Node that) {
      return Math.sqrt(Math.pow(this.X - that.X, 2) + Math.pow(this.Y - that.Y, 2));
    }
  }
}