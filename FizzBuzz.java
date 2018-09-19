/*	Turner Atwood
 *	9/6/18
 *	FizzBuzz [1.2]: (https://open.kattis.com/problems/fizzbuzz)
 */	

import java.util.Scanner;

class FizzBuzz{
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int first = in.nextInt();
		int second = in.nextInt();
		int num = in.nextInt();
		for (int i=1; i<=num; i++) {
			String line = "";
			if (i%first == 0) {
				line += "Fizz";
			}
			if (i%second == 0) {
				line += "Buzz";
			}
			if (line.equals("")) {
				line = Integer.toString(i);
			}
			System.out.println(line);

		}
	}
}