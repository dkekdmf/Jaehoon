T = int(input())

for i in range(T):
    a = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    
    print(f'#{i+1}',end = ' ')
    
    for i in range(a):
        print(lst[i],end= ' ')
    print()
    