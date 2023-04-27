a= int(input())
lst = list(map(int, input().split()))
lst1 = []
lst1.append(lst[0])

for i in range(1,a):
    lst1.append((lst[i]*(i+1))-sum(lst1))
for i in lst1:
    print(i,end = ' ')
