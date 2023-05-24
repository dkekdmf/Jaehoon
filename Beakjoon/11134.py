N = int(input())
for i in range(N):
    a,b = map(int, input().split())
    c = a//b + a%b
    print(a//b +  (1 if a%b else 0))
    