a= int(input())
array = set(map(int,input().split()))
b= int(input())
lst1 = list(map(int,input().split()))

for i in lst1:
    if i in array:
      print('1')
    else:
      print('0')
       