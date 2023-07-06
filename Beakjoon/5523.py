T = int(input())
count1,count2 = 0,0
for i in range(T):
  
    a,b = map(int, input().split())
    if a>b:
        count1 +=1
    elif a<b:
        count2+=1
    else:
        continue
print(count1,count2)