/*	Turner Atwood
 *	10/19/18
 *	Simplicity [2.6] (https://open.kattis.com/problems/simplicity)
 */

import java.util.Scanner;
import java.util.Arrays;


// Find how many characters need to be deleted to 
//	leave a string with at most 2 distinct characters
class Simplicity {

	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int[] letterFrequencies = new int[26];

		//Initialize all letter frequencies  to 0
		for (int i = 0; i < 26; i++) {
			letterFrequencies[i] = 0;
		}

		//Build the letter frequency map off of the input
		String word = in.nextLine();
		for (int i = 0; i < word.length(); i++) {
			char letter = word.charAt(i);
			letterFrequencies[(int)letter-97] += 1;
		}

		//Sort the array (ascending)
		Arrays.sort(letterFrequencies);

		//Subtract length from the frequencies of the two most common letters
		int lettersLeft = letterFrequencies[25] + letterFrequencies[24];
		System.out.println(word.length()-lettersLeft);
	}
}