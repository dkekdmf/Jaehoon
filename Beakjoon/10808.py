# alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
# 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# count = 0

# for i in alph_list:
#     if  alph_list in lst1[i]:
#         count+=1
#     print(count)
lst1 = list(input())  
lst2 = []
for i in lst1:
    lst2.append(ord(i))
print(lst2)

    