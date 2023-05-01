a,b,c = map(int, input().split())

result =(a*b)-c
if a*b <=c:
    result = 0
print(result)
