N,M = map(int,input().split())

set1 = set()
count = 0
for _ in range(N):
    data = input()
    set1.add(data)
for _ in range(M):
    data1 = input()
    if data1 in set1:
        count+=1
print(count+1)