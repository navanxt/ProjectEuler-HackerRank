import sys
t = int(input().strip())
for a0 in range(t):
    sum = 0
    n = int(input().strip())
    for i in range(n):
        if i%3==0 or i%5==0:
            sum+=i
    print(sum)
