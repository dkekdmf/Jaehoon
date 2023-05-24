n = int(input())
for i in range(n):
    ans = 0
    # a,b,c = map(int,input().split())
    # max1 = max(a,b,c)
    lst = list(map(int,input().split()))
    lst.sort()
    if lst[2]**2 == lst[0]**2+lst[1]**2:
        ans = 'yes'   
    else:
        ans = 'no'
    print('Scenario #{}:\n{}\n'.format(i+1,ans))