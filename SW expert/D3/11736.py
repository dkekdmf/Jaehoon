T = int(input())

for i in range(T):
    a = int(input())
    lst = list(map(int, input().split()))
    # print(lst)
    ans = 0
    for t in range(1,len(lst)-1):
        if lst[t]!= max(lst[t],lst[t+1],lst[t-1]) and lst[t]!=min(lst[t],lst[t+1],lst[t-1]):
            ans+=1
    print('#{} {}'.format(i+1,ans))
    


        