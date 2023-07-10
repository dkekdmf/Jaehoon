N,B = map(int,input().split())
print(N,B)
ans = ""
while N>0:
    D = N%B
    if D<10: ans+=D
    else: ans+=chr((D-10+'A'))
    N=N/B
for i in range(len(ans)):
    print(ans[i])