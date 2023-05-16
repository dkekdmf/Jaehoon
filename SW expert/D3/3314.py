T = int(input())

for i in range(T):
    lst = list(map(int , input().split()))
    ans =0
    for j in lst:
        if j>=40:
            ans+= j
        else:
            ans+=40
        ans1 = ans//5
    print('#{} {}'.format(i+1,ans1))
