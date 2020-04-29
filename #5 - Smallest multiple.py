import sys

def smallest_multiple(n):
    flag = False
    flag1 = True
    i = int(1)
    while(not flag):
        for j in range(1,n):
            if i%j!=0:
                flag1 = False
        if(flag1):
            print(i)
            flag = True
            break
        else:
            i+=1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    smallest_multiple(n)

#to reduce time -->

from math import gcd
from functools import reduce

for _ in range(int(input())):
    N = int(input())
    print(reduce(lambda x,y: x*y//gcd(x,y), range(1,N+1)))
