#Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
#The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so.


def SieveOfEratosthenes(n): 
      
    
    
   
    prime = [True for i in range(n+1)]  # Create a boolean array "prime[0..n]" and initialize  all entries it as true. A value in prime[i] will 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False  # finally be false if i is Not a prime, else true. 
        p += 1
        
        
         # Print all prime numbers 
    for p in range(2, n+1): 
        if prime[p]: 
            print (p)
  
# driver program 
if __name__=='__main__': 
    n = 30
    print ("Following are the prime numbers smaller",) 
    print ("than or equal to", n )
    SieveOfEratosthenes(n) 
    # You can run the program by directly compying it on ide. Change the value of n for your desired result.
