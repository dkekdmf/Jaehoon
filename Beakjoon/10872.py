def factorial(n):
    result = 1
    if n>0:
       result = n*factorial(n-1)
    return result
    
a = int(input())

print(factorial(a))

# def factorial(num):
#     if num <=1:
#         return num
#     else:
#         return num*factorial(num-1)

# a = int(input())
# print(factorial(a))