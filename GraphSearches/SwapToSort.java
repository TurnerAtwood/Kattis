/*	Turner Atwood
 *	4/9/19
 *	Swap To Sort [3.8] : (https://open.kattis.com/problems/swaptosort)
 *	UNION-FIND
 */

import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;

class SwapToSort {
	static int[] parents;

	public static void main(String args[]) {
		Kattio in = new Kattio(System.in, System.out);

		int N = in.getInt();
		int K = in.getInt();
		parents = new int[N];

		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}

		int a,b;
		for (int i = 0; i < K; i++) {
			a = in.getInt();
			b = in.getInt();
			union(a-1,b-1);
		}

		// Find on every element to ensure the parents are the same
		for (int i = 0; i < N/2; i++) {
			a = find(i);
			b = find(N-1-i);
			if (a != b) {
				System.out.println("No");
				return;
			}
		}
		System.out.println("Yes");
	}

	static int find(int a) {
		if (parents[a] == a) {
			return a;
		}
		parents[a] = find(parents[a]);
		return parents[a];
	}

	static void union(int a, int b) {
		int p_a = find(a);
		int p_b = find(b);
		parents[p_b] = p_a;
	}
}

// Fast input more than doubles run speed
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