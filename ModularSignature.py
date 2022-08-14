import cmath
from timeit import default_timer as timer





def piFunction(n):
    primes = []       
    for i in range(2, n):
        if(isPrime(i)): 
            primes.append(i)                     
    return primes

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:            
            return False        
    else:
        return True



def primeFactorization(n):
    factors = []
    for i in range(2, n + 1):
        while(n % i == 0):
            factors.append(i)
            n //= i 
    return factors
    
def distinctPrimeFactorization(n):
    return sorted(set(primeFactorization(n)))



n = 452002

#primes = [piFunction(n)]








start = timer()



end = timer()
print("Time1: ", end - start)

start2 = timer()

primes = piFunction(n)

end2 = timer()
print("Time2: ", end2 - start2)