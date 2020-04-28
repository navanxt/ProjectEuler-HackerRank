#!/bin/python3

import sys

def Largest_Prime_Factor(n):
    prime_factor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1

    if prime_factor < n:
        prime_factor = n

    return int(prime_factor)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(Largest_Prime_Factor(n))
