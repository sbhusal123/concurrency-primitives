# spiliting the workload

import time
import random

from multiprocessing import Process

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


def calculate(numbers):
    for i in numbers:
        result = calculatePrimeFactors(i)
        print(f"{i} prime factorized = {result}")

def chunk_list(arr, chunk_size):
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

def main():
    print("Starting number crunching..")
    t0 = time.time()

    numbers = []

    for i in range(10000):
        rand = random.randint(20000, 100000000)
        numbers.append(rand)

    # chunking array into 10 separate arrays
    splitted_input = chunk_list(numbers, 10)

    processes = []
    for chunk in splitted_input:
        p = Process(target=calculate, args=(chunk, ))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    
    t1 = time.time()

    total_time = t1 - t0

    print("Execution Time: {}".format(total_time))

if __name__ == "__main__":
    main()
