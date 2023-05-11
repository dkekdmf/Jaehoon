N = int(input())
a= 1
result =0
sum = 0
lst = list(map(int, input().split()))

for i in range(N):
    if lst[i] ==1:
        sum+=1
        result+=sum
    else:
        sum = 0
print(result)

# for i in lst:
#     if lst[i] == 0:
#         result.append(1)
#     elif lst[i] ==1:
#         result.append(0)
#     if lst[i]==lst[i+1]:
#        lst[i] = lst[i]+1
#        result.append(lst[i])
# print(result)

