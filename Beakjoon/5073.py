# while True:
#     a,b,c = map(int , input().split())
    
#     if a==0 and b==0 and c==0:
#         break
#     if a==b==c:
#         print('Equilateral')
#     elif a==b or b==c or a==c:
#         print('Isosceles')
#     elif a!=b and b!=c and c!=a:
#         print('Scalene')   

while True:
  lst = sorted(list(map(int ,input().split())))
  print(lst)
  if lst[0] ==0 and lst[1] == 0 and lst[2]==0:
      break
  elif lst[0]+lst[1]<=lst[2]:
          print('Invalid') 
          
  elif lst[0]==lst[1]==lst[2]:
      print('Equilateral')
  elif lst[0]==lst[1] or lst[1]==lst[2] or lst[0]==lst[2]:
      print('Isosceles')
  elif lst[0]!=lst[1] and lst[1]!=lst[2] and lst[2]!= lst[0]:
      print('Scalene')   
  

