T = int(input())

for i in range(T):
    lst = list(map(int,input().split()))
    print(f'#{i+1} {max(lst)}')
    