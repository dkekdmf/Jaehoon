a,b = map(int,input().split())
if a<b:
    for index in range(a,b+1):
         print(index)
elif a>b:
    for index in range(b,a+1):
         print(index)
elif a==b:
    print(a)