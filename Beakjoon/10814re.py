
array= []
for i in range(int(input())):
    input1 = input().split()
    array.append((int(input1[0]),input1[1]))
   
   
array= sorted(array,key = lambda x : x[0])  

for i in array:
    print(i[0],i[1])