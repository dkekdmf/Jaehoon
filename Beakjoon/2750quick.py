def qsort(data):
    if len(data)<=1:
        return data
    left,right = list(),list()
    pivot = data[0]
    for i in range(1,len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return qsort(left) + [pivot]+ qsort(right)
N  = int(input())
M = []
for i in range(N):
    M.append(int(input()))
data = qsort(M)
for i in range(len(data)):
    print(data[i])
