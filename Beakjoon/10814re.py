N = int(input())
lst2 = []
for i in range(N):
   lst = input().split()
   lst2.append((int(lst[0]),lst[1]))
print(lst2)
lst2.sort(key=lambda x:(x[0],x))
for i in lst2:
    print(i[0],i[1])