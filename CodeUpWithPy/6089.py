a,r,n = map(int, input().split())

for i in range(n+1):
    c = a*(r**(n-1))
print(c)