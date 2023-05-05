N = int(input())
array = []
for i in range(N):
    a= input().split()
    array.append((int(a[0]),a[1]))
array1 = sorted(array,key = lambda x:x[0])
array2 = sorted(array1,key = lambda x:x[1])
for i in array2:
    print(i[0],i[1])

# N = int(input())
# array = []
# for _ in range(N):
#     x,y = map(int,input().split())
#     array.append((x,y))
# array = sorted(array)
# for i in array:
#     print(i[0],i[1])
    
    