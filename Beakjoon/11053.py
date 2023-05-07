n = int(input())
array = list(map(int,input().split()))
dp = [1]*n
for i in range(1,n):
    for k in range(0,i):
        if array[k]<array[i]:
            dp[i] = max(dp[i],dp[k]+1)
print(max(dp))