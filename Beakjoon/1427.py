# lst = list(map(int,input()))

# lst.sort()
# lst.reverse()

# for i in lst:
#     print(i,end = '')
    
array = input()

for i in range(9,-1,-1):
    for j in array:
        if int(j) == i:
            print(i,end='')