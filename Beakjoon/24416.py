
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fibo1(n):
    dp = [0 for index in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    count = 0
    for index in range(3,n+1):
        count+=1
        dp[index] = dp[index-1] + dp[index-2]
    return count
n = int(input())
print(fib(n),fibo1(n))   
    
    
