n = int(input())
N = sorted(list(map(int,input().split())))
x = int(input())
left,right = 0,n-1
ans = 0
while left<right:
    temp = N[left] + N[right]
    if temp == x:
        ans+=1
        left+=1
    elif temp <x:
        left+=1
    else:
        right-=1
print(ans)
    