T = int(input())
for i in range(T):
    a = int(input())
    dp  = [0]*101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    for index in range(5,101):
        dp[index] = dp[index-2]+ dp[index-3]
    print(dp[a])