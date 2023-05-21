while True:
    a,b,c = map(int , input().split())
    if a ==0 and b ==0 and c==0:
        break
  
    
    if a*a + b*b == c*c:
        print('right')
    else:
        print('wrong')

while True:
    lst = list(map(int, input().split()))
    if lst[0] ==0 and lst[1] ==0 and lst[2] == 0:
        break
    lst.sort()

    if lst[0]*lst[0] + lst[1]*lst[1] == lst[2]*lst[2]:
        print('right')
    else:
        print('wrong')