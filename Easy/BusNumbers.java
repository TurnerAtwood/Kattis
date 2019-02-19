/*	Turner Atwood
 *	2/19/19
 *	Bus Numbers [2.6]: (https://open.kattis.com/problems/busnumbers2)
 *	Try all numbers below M by generating the cubes
 *		up to 400000 and searching from both ends
 */

import java.util.*;

class BusNumbers {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int M = in.nextInt();
		ArrayList<Integer> cubes = generateCubes();

		// Find the highest bus number under N
		int found = 0;
		for (int i = M; i >= 0; i--) {
			if (isBusNumber(i, cubes)) {
				found = i;
				break;
			}
		}

		if (found != 0) {
			System.out.println(found);
		}
		else {
			System.out.println("none");	
		}
	}

	// List of all cubes under 400,000
	static ArrayList<Integer> generateCubes() {
		ArrayList<Integer> cubes = new ArrayList<Integer>();
		int cube = 1;
		int i = 2;
		while (cube < 400000) {
			cubes.add(cube);
			cube = i*i*i;
			i++;
		}
		return cubes;
	}

	// Determine if a number is a bus number
	static boolean isBusNumber(int a, ArrayList<Integer> cubes) {
		int left = 0;
		int right = cubes.size()-1;
		int count = 0;
		int potential;
		while (left <= right) {
			potential = cubes.get(left) + cubes.get(right);
			if (potential < a) {
				left++;
			}
			else if (potential > a) {
				right--;
			}
			else {
				count++;
				left++;
				if (count == 2) {
					return true;
				}
			} 
		}
		return false;
	}
}