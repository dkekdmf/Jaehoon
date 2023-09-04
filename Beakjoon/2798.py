a,b = list(map(int, input().split()))
data1 = list(map(int , input().split()))

result = 0
length = len(data1)
for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum = data1[i] + data1[j] + data1[k]
            if sum<=b:
                result = max(result,sum)
print(result)