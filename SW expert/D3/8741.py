T = int(input())

for i in range(T):
    lst = list(input().split())
    ans = lst[0][0] + lst[1][0] + lst[2][0]
    ans1 = ans.upper()
    print('#{} {}'.format(i+1,ans1))
        