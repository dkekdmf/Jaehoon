N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst1 = list(map(int , input().split()))

for item in lst1:
     if item in lst:
         print(1)
     else:
        print(0)