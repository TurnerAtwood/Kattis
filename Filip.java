/*	Turner Atwood
 *	9/6/18
 *	Filip [1.2]: (https://open.kattis.com/problems/filip)
 */	

// Scanner is used to get input for the function (Using Standard-In)
import java.util.Scanner;

//Make sure that the class name is the same as the .java file name
class Filip {
	public static void main(String args[]) {
		// Create our Scanner to get input
		// NOTE - notice how we are using "System.in", and not reading from a file
		Scanner in = new Scanner(System.in);

		// Read in the two numbers as strings
		// NOTE - look up java.util.Scanner if you haven't used this before
		String first_string = in.next();
		String second_string = in.next();

		// Reverse the numbers using a method defined below
		// NOTE - notice how we can call this two different ways here.
		//		  This works because the method is a static method of Filip.
		first_string = Filip.reverseString(first_string);
		second_string = reverseString(second_string);
	
		// Convert the numbers from strings into integers
		// NOTE - we have to use the static methods from the "Integer" class
		int first_int = Integer.parseInt(first_string);
		int second_int = Integer.parseInt(second_string);

		//Compare the numbers and print the larger
		// NOTE - we have to use integers to use the ">" operator
		if (first_int > second_int) {
			// NOTE - this could use first_string ~OR~ first_int, it doesn't matter!
			System.out.println(first_int);
		}
		else {
			System.out.println(second_int);
		}
	}

	// This is a method that takes a String and returns the input string in reverse
	// NOTE - notice that this method is static, this means we don't have to
	//		  make an instance of the Filip class to use it!
	public static String reverseString(String input) {
		
		String output = "";
		int length = input.length();
		
		// This for loop will go through the input string in reverse
		for (int i = length - 1; i >= 0; i--) {
			
			// We take one character at a time with the substring method
			// We append that one-character String to output using "+="
			output += input.substring(i,i+1);
			// Same as: output = output + input.substring(i,i+1);
		}

		return(output);
	}
}