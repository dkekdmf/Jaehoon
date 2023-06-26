import sys

n = int(input())
k  = int(input())


if k>=n:
    print(0)
    sys.exit()
    
array = list(map(int, input().split(' ')))
array.sort()

distance =[]

for i in range(1,n):
    distance.append(array[i]- array[i-1])
    distance.sort(reverse=True)
for i in range(k-1):
    distance[i] = 0
print(sum(distance))