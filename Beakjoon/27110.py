N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(3):
    if A[i]<=N:
        count+= A[i]
    elif A[i]>N:
        count+=N
print(count)
        