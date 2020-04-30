import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prime_numbers = [2,3]
    i=3
    if(0<n<3):
        print(prime_numbers[n-1])
    elif(n>2):
        while (True):
            i+=1
            status = True
            for j in range(2,int(i/2)+1):
                if(i%j==0):
                    status = False
                    break
            if(status==True):
                prime_numbers.append(i)
            if(len(prime_numbers)==n):
                break
        print(prime_numbers[n-1])
        
#to reduce time -->

def prime(n,prime_numbers):
    x=prime_numbers[len(prime_numbers)-1]
    while len(prime_numbers)<n:
        x+=2
        y=math.floor(x**0.5)
        count=0
        for i in prime_numbers:
            if i>y:
                count=0
                break
            if x%i==0:
                count=1
                break
        if count==0:
            prime_numbers.append(x)
    return prime_numbers

t=int(input())
prime_numbers=[2,3]
for i in range(t):
    n=int(input())
    if len(prime_numbers)<n:
        prime_numbers=prime(n,prime_numbers)
    print(prime_numbers[n-1])
