n,k = map(int,input().split())
ans = []
max= 0
for i in range(1,k+1):
    ans.append(int(str(n*i)[::-1]))
for i in range(len(ans)):
    if ans[i]>max:
        max = ans[i]
print(max)
