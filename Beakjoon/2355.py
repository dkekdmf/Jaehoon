A,B = map(int, input().split())
sum = 0
for i in range(A,B+1):
    sum+=i
print(sum)

a,b = map(int,input().split())
if a>b:
    a,b=b,a
print(b*(b+1)//2-a*(a-1)//2)