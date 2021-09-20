"""
/*  Turner Atwood
 *  9/11/2021
 *  Blackboard Numbers [4.2] (https://open.kattis.com/problems/primes2)
 *  Ad-hoc - Just try to interpret as all 4 bases and count how many are prime
 */
"""

bases = [2,8,10,16]
def prime_prob(num):
    try:
        if int(num) < 2:
            return "0/1"
    except:
        pass

    valid_bases = 0
    prime_bases = 0
    for base in bases:
        try:
            dec = int(num, base)
        except:
            continue
        valid_bases += 1
        if is_prime(dec):
            prime_bases += 1

    # Format output (prime_bases / valid_bases)
    gcd = get_gcd(prime_bases, valid_bases)
    top = prime_bases//gcd
    bot = valid_bases//gcd
    return f"{top}/{bot}"

def get_gcd(x,y):
    while y:
        x, y = y, x % y
    return x

def is_prime(num):
    i = 2
    while(i*i <= num):
        if num/i == num//i:
            return False
        i += 1
    return True

def main():
    for _ in range( int(input()) ):
        num = input()
        print(prime_prob(num))
        

if __name__ == "__main__":
    main()

