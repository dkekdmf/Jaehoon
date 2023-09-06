cnt = [i for i in range(1,31)]

for _ in range(28):
    ap = int(input())
    cnt.remove(ap)
print(min(cnt))
print(max(cnt))

