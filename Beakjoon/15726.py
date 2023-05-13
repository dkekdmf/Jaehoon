lst = list(map(int, input().split()))
# lst.sort()
mul =1
# print(lst[-1]*lst[1]//lst[0])
c = min(lst)
lst.remove(min(lst))
for i in lst:
    mul*= i
print(mul//c)

A, B, C = map(int, input().split())
print(A * max(B, C) // min(B, C))