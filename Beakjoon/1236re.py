n, m  = map(int,input().split())
array = []
existRowCount = 0
existColCount = 0

for _ in range(n):
    array.append(input())
    
for i in range(n):
    exist = False
    for j in range(m):
        if array[i][j] == 'X':
            exist = True
            break
    if exist:
        existRowCount+=1
for j in range(m):
    exist = False
    for i in range(n):
        if array[i][j] == 'X':
            exist = True
            break
    if exist:
        existColCount+=1
        
needRowCount = n-existRowCount
needColCount = m-existColCount
print(max(needColCount,needRowCount))

