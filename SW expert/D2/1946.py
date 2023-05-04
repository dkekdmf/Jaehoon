
lst = list(input().split())
lst1 = list(input().split())
lst2 = list(input().split())
lst.append(lst[0]*int(lst[1]))
lst1.append(lst1[0]*int(lst1[1]))
lst2.append(lst2[0]*int(lst2[1]))

if int(lst1[1])<10:
       lst1.append(lst2[0]*(10-int(lst1[1])))
       lst2.pop(lst2[0]*(10-int(lst1[1])))
for i in lst,lst1,lst2:
    print(i,end = ' ')