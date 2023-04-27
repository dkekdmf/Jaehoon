a= int(input())

for j in range(1,a+1):
    lst = map(int, input().split())
    sum = 0
    for i in lst:
         if i%2!=0:
             sum+=i
    print("#"+str(j),str(sum))