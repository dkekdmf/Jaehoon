
arr = []
for i in range(int(input())):
    x,y = map(int,input().split())
    arr.append((x,y))
arr = sorted(arr)

for i in arr:
    print(i[0],i[1])