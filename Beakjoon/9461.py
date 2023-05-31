n = int(input())
dp = [0]*101
dp[1] =1
dp[2] =1
dp[3] =1
dp[4]= 2
for i in range(n):
    p = int(input())
    for index in range(5,101):
     dp[index] = dp[index-2]+ dp[index-3]
    print(dp[p])