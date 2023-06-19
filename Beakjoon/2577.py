a = int(input())
b= int(input())
c= int(input())
result = str(a*b*c)
#첫번째 방법
print(result.count('0'))
print(result.count('1'))
print(result.count('2'))
print(result.count('3'))
print(result.count('4'))
print(result.count('5'))
print(result.count('6'))
print(result.count('7'))
print(result.count('8'))
print(result.count('9'))

for i in result:
    print(result.count(str(i)))



#두번째 방법
# for i in range(10):
#     print(result.count(str(i)))