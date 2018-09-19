/*	Turner Atwood
 *	9/6/18
 *	AboveAverage [2.0]: (https://open.kattis.com/problems/aboveaverage)
 */	

import java.util.Scanner;
import java.util.Collections;
import java.util.Arrays;

class AboveAverage {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int fnum = in.nextInt();
		for (int z=0; z<fnum; z++) {
			int num = in.nextInt();
			double[] grades = new double[num+1];
			double avg = 0;
			for (int i=0; i< num; i++) {
				int grade = in.nextInt();
				grades[i] = grade;
				avg += grade;
			}
			avg = avg/num;
			grades[num] = avg;
			
			Arrays.sort(grades);
			int spot = 0;
			for (int i=num; i>=0; i--) {
				if (grades[i] == avg) {
					spot = i;
					i = -1;
				}
			}
			double percent = (num-spot)*100.0/num;
			System.out.printf("%.3f", percent);
			System.out.println("%");
		}
	}
}