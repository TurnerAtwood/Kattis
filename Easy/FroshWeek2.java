/*	Turner Atwood
 *	10/21/18
 *	Frosh Week [2.6] (https://open.kattis.com/problems/froshweek2)
 *
 */

import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.ArrayList;

class FroshWeek2 {
	public static void main(String args[]) {
		// Input
		Scanner in = new Scanner(System.in);
		StringTokenizer st = new StringTokenizer(in.nextLine());
		int taskNum = Integer.parseInt(st.nextToken());
		int intervalNum = Integer.parseInt(st.nextToken());
		int[] tasks = new int[taskNum];
		int[] intervals = new int[intervalNum];
		
		// Multiply by -1 to reverse the order when sorting
		st = new StringTokenizer(in.nextLine());
		for (int i = 0; i < taskNum; i++) {
			tasks[i] = -1*Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(in.nextLine());
		for (int i = 0; i < intervalNum; i++) {
			intervals[i] = -1*Integer.parseInt(st.nextToken());
		}

		// Sort the arrays and intervals
		Arrays.sort(tasks);
		Arrays.sort(intervals);

		// Start with longer tasks for longer intervals
		//	Find the max amount of tasks we can complete
		int count = 0;
		int taskIndex = 0;
		for (int i = 0; i < intervalNum; i++) {
			int interval = -1*intervals[i];
			int task = -1*tasks[taskIndex];
			
			// Find the first task that works for the given interval
			while (task > interval) {
				taskIndex++;
				if (taskIndex == taskNum) {
					break;
				}
				task = -1*tasks[taskIndex];
			}
			count++;
			taskIndex++;

			// Ran out of tasks
			if (taskIndex > taskNum) {
				count--;
				break;
			}
			// Completed all tasks
			if  (taskIndex == taskNum) {
				break;
			}
		}
		
		System.out.println(count);
	}

}