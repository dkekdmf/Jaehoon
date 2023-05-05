N = int(input())
lst2 = []
for i in range(N):
   lst1 = input().split(' ')
   lst2.append((int(lst1[0]),lst1[1]))
lst2 = sorted(lst2, key =lambda x:x[0])
for i in lst2:
    print(i[0],i[1])

 
   
   