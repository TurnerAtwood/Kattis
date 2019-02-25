"""
/*	Turner Atwood
 *	2/??/19
 *	Palindromic Password [3.5] : (https://open.kattis.com/problems/palindromicpassword)
 *	Extremely basic BFS
 */
"""

def main():
	N = int(input())
	for z in range(N):
		num = int(input())
		i = 0
		# Try num += i for i in {0,1,2,...}
		while (True):
			down = num - i
			if down >= 100000 and isPalindrome(down):
				print(down)
				break
			up = num + i
			if up <= 999999 and isPalindrome(up):
				print(up)
				break
			i += 1

# Simplest way to check if a number is a palindrome
## (Forward string == String in reverse)
def isPalindrome(number):
	return str(number) == str(number)[::-1]

if __name__ == "__main__":
	main()