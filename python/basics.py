# # ## printing statement
# # # #a=12
# # # #print(a)

# # ## factorial sum
# # # #def factorial(num):
# # #    # if num==1 or num==0:
# # #    #     return 1
# # #   #  else:
# # #  #       return num*factorial(num-1)
# # # #num=5
# # # #print(factorial(num))

# # ## 
# # # #n=5
# # # #for i in range(1,n+1,2):
# # # #    print(i)



# # n=5
# # for i in range(1,n+1,2):
# #     print(i)

# # # #n=int(input("enter a number"))
# # # #a, b = 0, 1
# # # #while a <= n:
# # #  #   print( a, end=" ")
# # #  #   a,b = b , a + b


# # # #a=7
# # # #b=5
# # # #print(f"before swapping {a} and {b}")
# # # #temp=a
# # # #a=b
# # # #b=temp
# # # #print("a:",a)
# # # #print("b:",b)
# # # #print(f"after swapping {a} and {b}")



# # # #num1=int(input("enter a num1:"))
# # # #num2=int(input("enter a num2:"))
# # # #num3=int(input("enter a num3:"))
# # # #if num1 >= num2:
# # # #    print(F"{num1} is a largest number")
# # # #elif num2 >= num3:
# # # #    print(F"{num2} is a largest number")
# # # #else:
# # #  #   print(f"{num3} is a largest number")




# # # a=4
# # # b=str(a)
# # # print(type(b))




# # # def factorial(n):
# # #     if n==1 or n==0:
# # #         return 1
# # #     else:
# # #         return n*factorial(n-1)
# # # def is_Strong_number(num):
# # #     original_num=num
# # #     sum_factorial = 0
# # #     while num > 0:
# # #         digit = num % 10
# # #         sum_factorial += factorial(digit)
# # #         num=num//10
# # #     return original_num == sum_factorial
# # # num=int(input("enter a number:"))
# # # if is_Strong_number(num):
# # #     print(f"{num} is a strong number")
# # # else:
# # #     print(f"{num} is not a strong number")





# n=4
# if n > 3:
#     print("greater")
# else:
#     print("lesser")




dict = {"name": "vivek", 
        "age": 21, 
        "marks": 530}
print(dict.values())
print(dict.keys())
print(dict)
dict.update({"city": "Hyderabad"})
print(dict)
dict.pop("marks")
print(dict)
dict1 = dict.popitem()
print(dict)
city=dict.setdefault("hyderabad")
print(city)