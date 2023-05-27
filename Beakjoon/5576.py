
ans = []
ans1 = []
for i in range(10):
    a = int(input())
    ans.append(a)
# print(ans)
for j in range(10):
    b = int(input())
    ans1.append(b)
ans.sort()
ans1.sort()
t = ans[-1] + ans[-2] + ans[-3]
w = ans1[-1] + ans1[-2] + ans1[-3]
print(t,w)
