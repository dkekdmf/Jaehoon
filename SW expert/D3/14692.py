TC = int(input())
ans = ''
for i in range(TC):
    a = int(input())
    
    if a %2 == 0:
       ans = 'Alice'
    else:
        ans = 'Bob'
    print('#{} {}'.format(i+1,ans))