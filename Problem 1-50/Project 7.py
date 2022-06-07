"""
Problem 7 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
count=0

def primeornot(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                #it is not prime
                return False
                break
        else:
            #it is prime
            return True
    else:
        return False
    
i=0
while count<10002:
    if primeornot(i):
        count+=1
    i+=1

print(i-1)
