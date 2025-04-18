T = int(input())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(T):
    n = int(input())
    for index in range(4,11):
        dp[index] = dp[index-1] + dp[index-2] + dp[index-3]
    print(dp[n])