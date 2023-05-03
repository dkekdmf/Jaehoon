T = int(input())
# a= ['<','=','>']
for i in range(T):
    lst = list(map(int,input().split()))
    if lst[0]>lst[1]:
       a = '>'
    elif lst[0]<lst[1]:
       a= '<'
    else:
      a= '='
    print(f'#{i+1} {a}')
    