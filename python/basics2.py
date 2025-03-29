# # # # ## addition using numpy

# # # # # # # # # #import pandas as pd
# # # # # # # # #import numpy as np
# # # # # # # # #a=np.array([2,4,5,6])
# # # # # # # # #b=np.array([4,6,7,8])
# # # # # # # # #c=a+b
# # # # # #print(c)



# # # # ## using pow function with two variable

# # # # # # # # #import math

# # # # # # # # #a=2
# # # # # # # # #b=2
# # # # # # # # #c=pow(a,b)
# # # # # # # # #print(c)



# # # # ## srong number

# # # # # # # # def factorial(n):
# # # # # # # #     if n==1 or n==0:
# # # # # # # #         return 1
# # # # # # # #     else:
# # # # # # # #         return n*factorial(n-1)
# # # # # # # # def is_Strong_number(num):
# # # # # # # #     original_num=num
# # # # # # # #     sum_factorial = 0
# # # # # # # #     while num > 0:
# # # # # # # #         digit = num % 10
# # # # # # # #         sum_factorial += factorial(digit)
# # # # # # # #         num=num//10
# # # # # # # #     return original_num == sum_factorial
# # # # # # # # num=int(input("enter a number:"))
# # # # # # # # if is_Strong_number(num):
# # # # # # # #     print(f"{num} is a strong number")
# # # # # # # # else:
# # # # # # # #     print(f"{num} is not a strong number")




# # # # ## factorial number

# # # # # # # # def fact(n):
# # # # # # # #     if n==1 or n==0:
# # # # # # # #         return 1
# # # # # # # #     else:
# # # # # # # #         return n*fact(n-1)
# # # # # # # # num=int(input("enter a number:"))
# # # # # # # # print(fact(num))



# # # # ## palindrome number with number

def is_palindrome(num):
    return str(num) == str(num)[::-1]
num=int(input("enter a num value:"))
if is_palindrome(num):
    print(f"{num} is aplindrome:")
else:
    print(f"{num} is not a palindrome:")


# # # # ## palindrome using string

# # # # # # # def is_palindrome(s):
# # # # # # #     return s == s[::-1]
# # # # # # # s=input("enter a string:")
# # # # # # # if is_palindrome(s):
# # # # # # #     print(f"{s} is a palindrome")
# # # # # # # else:
# # # # # # #     print(f"{s} is not a palindrome")


# # # # ## fibonacci series

# # # # # # n=int(input("enter a number"))
# # # # # # a,b=0,1
# # # # # # while a < n:
# # # # # #     print(a,end=" ")
# # # # # #     a, b = b, a+b


# # # # ## fibonacci series within range
# # # # # start = int(input("enter a start value:"))
# # # # # end=int(input("enter a end value:"))
# # # # # a,b=0,1
# # # # # while a < end:
# # # # #     if a > start:
# # # # #         print(a,end=" ")
# # # # #     a, b = b,a+b


# # # # n=5
# # # # for i in range(n+1):
# # # #     print(i)




# # import math

# # num = int(input("Enter a number: "))
# # square = math.pow(num, 2)
# # print("Square of", num, "is", square)




# def function(a,b):
#     return a+b
# function(5,4)


# def palindrome(num):
#     return str(num) == str(num)[::-1]
# num=int(input("enter a number:"))
# if palindrome(num):
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")