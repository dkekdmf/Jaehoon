import sys

input = sys.stdin.readline
lst = []
MAX = -1
for _ in range(9):
    lst.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
       if lst[i][j] > MAX:
           MAX = lst[i][j] 
           
           X = i+1
           Y = j+1
print(MAX)
print(X,Y)
            