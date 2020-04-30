import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum1 = int(0)
    sum2 = int(0)
    sumsq = int(0)
    for i in range(0,n+1):
        sum1+=i
        sum2+=(i*i)
    sumsq = (sum1*sum1)
    print(abs(sumsq-sum2))
    
#to reduce time-->

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum1=n*(n+1)*(2*n+1)//6
    sum2=n*(n+1)//2
    print(abs((sum2*sum2)-sum1))
