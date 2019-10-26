/*	Turner Atwood
 *	10/17/19
 *	George [2.0] https://open.kattis.com/problems/george 
 *	Modified Dijkstra's 
 *	Very Rusty Java code
 */

import java.util.*;
import java.io.*;
@SuppressWarnings("unchecked")

public class George {
	public static void main(String args[]) {
		Kattio io = new Kattio(System.in, System.out);
		
		int N = io.getInt() + 1;
		int M = io.getInt();
		Map<Integer,Integer>[] nodes = new HashMap[N];
		for (int i = 0; i < N; i++) {
			nodes[i] = new HashMap<>();
		}

		int A = io.getInt();
		int B = io.getInt();
		int K = io.getInt();
		int G = io.getInt();

		// Get George Path Sequence
		int[] georgeSeq = new int[G];
		for (int i = 0; i < G; i++) {
			georgeSeq[i] = io.getInt();
		}

		// Get Roads
		int one,two,cost;
		for (int i = 0; i < M; i++) {
			one = io.getInt();
			two = io.getInt();
			cost = io.getInt();
			nodes[one].put(two,cost);
			nodes[two].put(one,cost);
		}

		// Determine when (start time) George is using each path
		Map<Integer,Integer>[] george = new HashMap[N];
		for (int i = 0; i < N; i++) {
			george[i] = new HashMap<>();
		}

		int total = 0;
		for (int i = 0; i < G-1; i++) {
			one = georgeSeq[i];	
			two = georgeSeq[i+1];
			george[one].put(two,total);
			total += nodes[one].get(two);
		}

		Map<Integer,Integer> distances = new HashMap<>();
		Queue<Tuple> pq = new PriorityQueue<>();
		pq.offer(new Tuple(A,K));

		Tuple current;
		while (!pq.isEmpty()) {
			// Get the next closest node to the graph
			current = pq.poll();

			// If the node is visited, ignore it
			if (distances.containsKey(current.node)) {
				continue;
			}

			distances.put(current.node, current.dist);

			//If we have visited the end then quit
			if (current.node == B) {
				break;
			}

			Map<Integer,Integer> neighbors = nodes[current.node];
			int g_s = -1;
			for (int neigh : neighbors.keySet()) {
				if (distances.containsKey(neigh)) {
					continue;
				}

				cost = current.dist + neighbors.get(neigh);
				
				// Check to see if George takes this path
				g_s = -1;
				if (george[current.node].containsKey(neigh)) {
					g_s = george[current.node].get(neigh);
				}
				if (george[neigh].containsKey(current.node)) {
					g_s = george[neigh].get(current.node);
				}
				int g_e = g_s + neighbors.get(neigh);

				// Account for George if he is in the path when we are
				if (g_s != -1 && current.dist > g_s && current.dist < g_e) {
					cost += g_e - current.dist;
				}
				pq.offer(new Tuple(neigh, cost));
			}
		}

		System.out.println(distances.get(B) - K);
	}

	static class Tuple implements Comparable<Tuple> {
		int node;
		int dist;

		Tuple(int n, int d) {
			node = n;
			dist = d;
		}

		public int compareTo(Tuple other) {
			return this.dist - other.dist;
		}
	}
}

/* Kattio */
class Kattio extends PrintWriter {
    public Kattio(InputStream i) {
	super(new BufferedOutputStream(System.out));
	r = new BufferedReader(new InputStreamReader(i));
    }
    public Kattio(InputStream i, OutputStream o) {
	super(new BufferedOutputStream(o));
	r = new BufferedReader(new InputStreamReader(i));
    }

    public boolean hasMoreTokens() {
	return peekToken() != null;
    }

    public int getInt() {
	return Integer.parseInt(nextToken());
    }

    public double getDouble() { 
	return Double.parseDouble(nextToken());
    }

    public long getLong() {
	return Long.parseLong(nextToken());
    }

    public String getWord() {
	return nextToken();
    }

    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
	if (token == null) 
	    try {
		while (st == null || !st.hasMoreTokens()) {
		    line = r.readLine();
		    if (line == null) return null;
		    st = new StringTokenizer(line);
		}
		token = st.nextToken();
	    } catch (IOException e) { }
	return token;
    }

    private String nextToken() {
	String ans = peekToken();
	token = null;
	return ans;
    }
}