import time
import random

def calculatePrimeFactors(n):
    """
    What is prime factorization: https://www.cuemath.com/numbers/prime-factorization/
    """
    prime_fac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            prime_fac.append(d)
            n = n // d # Flor Division: 7 // 2 = 3
        d += 1

    if n > 1:
        prime_fac.append(n)
    
    return prime_fac

def main():
    print("Starting number crunching..")
    t0 = time.time()

    for i in range(10000):
        rand = random.randint(20000, 100000000)
        result = calculatePrimeFactors(rand)
        print(f"{rand} prime factorized = {result}")
    
    t1 = time.time()

    total_time = t1 - t0

    print("Execution Time: {}".format(total_time))

if __name__ == "__main__":
    main()
