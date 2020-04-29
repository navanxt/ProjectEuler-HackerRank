import sys

def compute(x):
    ans = max(i * j
        for i in range(100, x)
        for j in range(100, x)
        if str(i * j) == str(i * j)[ : : -1])
    print(ans)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    compute(n)

# to reduce time -->

palindromelist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in palindromelist:
            palindromelist.append(a)
palindromelist.sort()
length = len(palindromelist)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        t = int(input())
        for i in range(length - 1, -1, -1):
            if palindromelist[i] < t:
                print(palindromelist[i])
                break
