a = int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

# print(a,b,c,d,e)
print((a+b+c+d+e)//5)
lst = [a,b,c,d,e]
lst.sort()

print(*lst[2:3])