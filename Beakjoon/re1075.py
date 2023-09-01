A = input()
S = int(input())
ans = int(A[:-2]+'00')

while True:
    if ans %S == 0:
        break
    ans+=1
print(str(ans)[-2:])