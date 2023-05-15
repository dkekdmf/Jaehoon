TC = int(input())

for i in range(TC):
    a= int(input())
    count = 0
    lst1 = list(input())
    lst2 = list(input())
    
    # for i in lst1:
    #     if i not in lst2:
    #         count+=1
    # print(a- count)
    
    for j in range(a):
        if lst1[j]== lst2[j]:
         count +=1
    print('#{} {}'.format(i+1,count))
# a= int(input())
# count = 0
# for i in range(a):
 
#     lst1 = list(input())
#     lst2 = list(input())
#     # print(lst1,lst2)
#     if lst1[i] != lst2[i]:
#         count+=1
#     print(count)
    
# for i in List1 :
#     if i not in List2 :
#         print("List 2 not containing :")
#         print(i)

        