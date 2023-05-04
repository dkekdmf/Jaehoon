
while True:
    a = input()
    if a== '#':
        break
    count = 0
    for c in a:
        if c in  'aeiouAEIOU':
            count +=1
    print(count)


# lst2 = []
# while True:
#     lst1 = list(map(str,input().split()))
#     count = 0
#     lst2 = ['a','e','i''o','u']
#     if lst1 == lst2:
#         count+=1
    
#     if lst1 =='#':
#         break
# print(count)


# for i in range():
#     lst1 = list(map(str,input().split()))
#     count = 0
#     lst2 = ['a','e','i''o','u']
#     if lst1[i] == lst2[i]:
#         count+=1
    
#     if lst1 =='#':
#         break
# print(count)