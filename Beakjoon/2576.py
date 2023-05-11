sum1 = []

for i in range(1,8):
    a= int(input())
    if a%2==1:
      sum1.append(a)
if sum1:
    print(sum(sum1))
    print(min(sum1))
else:
    print(-1)
    
