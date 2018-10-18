/*	Turner Atwood
 *	10/17/18
 *	Crane [6.3] (https://open.kattis.com/problems/crane2)
 *	Written in Java with optimized I/O (Python too slow)
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.lang.StringBuilder;

import java.io.DataInputStream; 
import java.io.FileInputStream; 
import java.util.Scanner; 

class Crane {
    // Better than passing them around in every parameter

    static int size;
    // crates[i] is the crate at spot i
    // crateisAt[i] is the location of crate i in crates
    static int[] crates;
    static int[] crateisAt;
    static ArrayList<String> moves;

    public static void main(String args[]) throws IOException{
        //BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Reader s = new Reader();
        int cases = s.nextInt();
        for (int z = 0; z < cases; z++) {

            // Set up a new test case
            size = s.nextInt();
            crates = new int[size];
            crateisAt = new int[size];
            moves = new ArrayList<String>();

            // Grab all crate info and save it off
            for (int i = 0; i < size; i++) {
                int crane = s.nextInt()-1;
                crates[i] = crane;
                crateisAt[crane] = i;
            }
            
            // Move every crate to its final position
            for (int i = 0; i < size; i++) {
                movetoSpot(i);
            }

            // Print all of the moves
            System.out.println(moves.size());
            StringBuilder result = new StringBuilder();
            for (String move : moves) {
                result.append(move);
            }
            System.out.print(result);
        }
    }

    // Move the selected crate to its final position
    static void movetoSpot(int crate) {
        while (crates[crate] != crate) {
            int index = crateisAt[crate];
            int dist = index - crate+1;
            String move;

            // Try and move directly to the final spot
            int farIndex = index+dist-2;
            if (farIndex < size) {
                swap(crate, farIndex);
                move = (crate+1) + " " + (farIndex+1);
            }

            // Move one to the left
            else if (dist%2 != 0) {
                swap(index-1, index);
                move = index + " " + (index + 1);
            }
            // Move halfway to the final spot
            else {
                swap(crate, index);
                move = (crate+1) + " " + (index + 1);
            }

            //Store each move made to print later
            moves.add(move+"\n");
        }
    }

    // Perform a swap over the indicated interval
    // Order doesn't change between the two halves
    static void swap(int start, int stop) {
        int dist = stop - start + 1;
        // Can't swap an odd interval
        if (dist%2 != 0) {
            System.out.println("ODD INTERVAL");
            return;
        }

        // Make the swap over the interval
        dist /= 2;
        for(int i = start; i < start + dist; i++) {
            int oppIndex = i + dist;
            int crate1 = crates[i];
            int crate2 = crates[oppIndex];

            crates[i] = crate2;
            crates[oppIndex] = crate1;

            crateisAt[crate1] = oppIndex;
            crateisAt[crate2] = i;
        }

    }
}

// Speedy I/O
class Reader 
{ 
	final private int BUFFER_SIZE = 1 << 16; 
	private DataInputStream din; 
	private byte[] buffer; 
	private int bufferPointer, bytesRead; 

	public Reader() 
	{ 
		din = new DataInputStream(System.in); 
		buffer = new byte[BUFFER_SIZE]; 
		bufferPointer = bytesRead = 0; 
	} 

	public Reader(String file_name) throws IOException 
	{ 
		din = new DataInputStream(new FileInputStream(file_name)); 
		buffer = new byte[BUFFER_SIZE]; 
		bufferPointer = bytesRead = 0; 
	} 

	public String readLine() throws IOException 
	{ 
		byte[] buf = new byte[64]; // line length 
		int cnt = 0, c; 
		while ((c = read()) != -1) 
		{ 
			if (c == '\n') 
				break; 
			buf[cnt++] = (byte) c; 
		} 
		return new String(buf, 0, cnt); 
	} 

	public int nextInt() throws IOException 
	{ 
		int ret = 0; 
		byte c = read(); 
		while (c <= ' ') 
			c = read(); 
		boolean neg = (c == '-'); 
		if (neg) 
			c = read(); 
		do
		{ 
			ret = ret * 10 + c - '0'; 
		} while ((c = read()) >= '0' && c <= '9'); 

		if (neg) 
			return -ret; 
		return ret; 
	} 

	public long nextLong() throws IOException 
	{ 
		long ret = 0; 
		byte c = read(); 
		while (c <= ' ') 
			c = read(); 
		boolean neg = (c == '-'); 
		if (neg) 
			c = read(); 
		do { 
			ret = ret * 10 + c - '0'; 
		} 
		while ((c = read()) >= '0' && c <= '9'); 
		if (neg) 
			return -ret; 
		return ret; 
	} 

	public double nextDouble() throws IOException 
	{ 
		double ret = 0, div = 1; 
		byte c = read(); 
		while (c <= ' ') 
			c = read(); 
		boolean neg = (c == '-'); 
		if (neg) 
			c = read(); 

		do { 
			ret = ret * 10 + c - '0'; 
		} 
		while ((c = read()) >= '0' && c <= '9'); 

		if (c == '.') 
		{ 
			while ((c = read()) >= '0' && c <= '9') 
			{ 
				ret += (c - '0') / (div *= 10); 
			} 
		} 

		if (neg) 
			return -ret; 
		return ret; 
	} 

	private void fillBuffer() throws IOException 
	{ 
		bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE); 
		if (bytesRead == -1) 
			buffer[0] = -1; 
	} 

	private byte read() throws IOException 
	{ 
		if (bufferPointer == bytesRead) 
			fillBuffer(); 
		return buffer[bufferPointer++]; 
	} 

	public void close() throws IOException 
	{ 
		if (din == null) 
			return; 
		din.close(); 
	} 
} 