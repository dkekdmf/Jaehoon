import sys

a = sys.stdin.readline()
for i in range(a):
    cnt = 0
    n,m = map(int,input().split())
   
    for i in range(1,n+1):
        for j in range(i+1,n):
            a= i
            b= j
            if ((a*a+b*b)+m)%(a*b)== 0:
                cnt+=1
    print(cnt)