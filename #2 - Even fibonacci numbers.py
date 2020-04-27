import sys
t = int(input().strip())
for a0 in range(t):
    i = 1
    j = 2
    new = 0
    sum = 0
    n = int(input().strip())
    while i<n:
        if i%2 == 0:
            sum+=i
        new = i+j
        i=j
        j=new
    print(sum)
