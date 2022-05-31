"""
Problem 4 Largest palindrome product
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


for i in range(100,1000):
    for j in range(100,1000):
        num=i*j
        reversed_num=0
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        if i*j==reversed_num:
            print(i*j)
