T = int(input())
ans = 0
for i in range(T):
    a,b,c = map(int ,input().split())
    if a==b:
        ans = c
    elif b==c:
       ans = a
    elif a==c:
       ans = b
    elif a==b==c:
       ans = a
    print('#{} {}'.format(i+1,ans))



