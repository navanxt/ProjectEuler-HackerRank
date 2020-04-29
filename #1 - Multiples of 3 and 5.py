import sys
t = int(input().strip())
for a0 in range(t):
    sum = 0
    n = int(input().strip())
    for i in range(n):
        if i%3==0 or i%5==0:
            sum+=i
    print(sum)
    
#to reduce time -->

t=int(input())
def ar(x):
    return x*(x+1);
for i in range(t):
    n =int(input())
    n -=1;
    a=int(n/3);
    b=int(n/5);
    c=int(n/15);
    print(int(int(3*ar(a) + 5*ar(b) - 15*ar(c))>>1));
