T = int(input())
ans = 0
for i in range(T):
    a = int(input())
    if a %2 ==1:
       ans = 'Odd'
    elif a%2 ==0:
        ans = 'Even'
    print('#{} {}'.format((i+1),ans))