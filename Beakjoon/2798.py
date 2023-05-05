a,b = list(map(int,input().split()))
data = list(map(int, input().split()))
result = 0

for i in range(1,len(data)):
    for j in range(i+1,len(data)):
        for k in range(j+1,len(data)):
            sum = data[i]+data[j]+data[k]
            if sum<=b:
                result = max(sum,result)
print(result)