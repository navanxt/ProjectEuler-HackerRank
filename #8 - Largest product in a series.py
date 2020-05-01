from operator import mul
import sys
from functools import reduce

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    number_list = [int(x) for x in str(num)]
    prod = []
    for i in range(0,len(number_list)-k):
        prod.append(reduce(mul,number_list[i:i+k]))
    print(max(prod))
