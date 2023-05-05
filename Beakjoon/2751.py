
def qsort(data):
    if len(data)<=1:
        return data
    left,right = list(),list()
    pivot = data[0]
    
    for index in range(1,len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    return qsort(left) + [pivot] + qsort(right) 

a = int(input())
M = []
for _ in range(a):
    M.append(int(input()))

M = qsort(M)
for i in M:
    print(i)

