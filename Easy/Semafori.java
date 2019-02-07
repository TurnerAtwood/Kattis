/*
	Turner Atwood
	2/7/19
	Semafori [2.2]: (https://open.kattis.com/problems/semafori)
	Trivial
*/

import java.util.*;

class Semafori {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);

		int N = in.nextInt();
		int len = in.nextInt();

		// [Location, Red time, Green time, Cycle Time]
		int[][] lights = new int[N][4];

		for (int i = 0; i < N; i++) {
			lights[i][0] = in.nextInt();
			lights[i][1] = in.nextInt();
			lights[i][2] = in.nextInt();
			lights[i][3] = lights[i][1]+lights[i][2];
		}

		//Now go from the start to the end
		int pos = 0;
		int time = 0;
		for (int i = 0; i < N; i++) {
			// Drive up to the light
			time += lights[i][0] - pos;
			pos = lights[i][0];

			// Check if the light is already green
			int cycleSpot = time%lights[i][3];
			if (cycleSpot >= lights[i][1]) {
				continue;
			}

			// Wait until the light turns green
			time += lights[i][1] - cycleSpot;
		}

		// Drive to the end of the road after the last light
		time += len - pos;
		System.out.println(time);
	}
}