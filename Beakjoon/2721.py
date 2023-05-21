def T(n):
    sum = 0
    for i in range(n+1):
         sum+=i
    return sum
     

S = int(input())

for i in range(S):
    a= int(input())
    sum = 0
    for i in range(1,a+1):
        k = i*T(i+1)
        sum+=k
    print(sum)

