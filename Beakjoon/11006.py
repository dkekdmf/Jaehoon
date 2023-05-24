T = int(input())
for i in range(T):
    N,M = map(int, input().split())
    S = M*2-N
    J = M-S
    print(S,J)
    