import sys

t = int(input().strip())
for a0 in range(t):
    sum_prime = int(0)
    n = int(input().strip())
    for num in range(n+1): 
        if num > 1: 
            flag = True
            for i in range(2,num):
                if (num % i) == 0:
                    flag = False
            if flag :
                sum_prime+=num
    print(sum_prime)
    
#to reduce time :-

import sys

limit = 1000000
suml = [0] * limit
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        suml[i] = suml[i-1] + i
        for n in range(i*i, limit, i):
            a[n] = False
    else:
        suml[i] = suml[i-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(suml[n])
