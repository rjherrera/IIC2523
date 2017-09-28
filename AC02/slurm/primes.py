#!/bin/python3
import sys, random

def is_prime(n):
    for i in range(2, int(n ** (1/2)) + 1):
        if not n % i:
            return False
    return True if n > 1 else False

n = int(sys.argv[1])
primes = [i for i in range(100 * n, 100 * (n + 1)) if is_prime(i)]
print(*primes, sep='\n')
