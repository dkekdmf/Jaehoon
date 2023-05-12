# lst = list(map(int, input().split()))
# lst2 = []
# max1 = max(lst)
# min1 = min(lst)
# lst2.append(max1)
# lst2.append(min1)
# lst.remove(max1)
# lst.remove(min1)
# sum1 = sum(lst2)
# sum2 = sum(lst)

# print(sum1-sum2)

a,b,c,d = map(int,input().split())
print(abs((a+d)-(b+c)))