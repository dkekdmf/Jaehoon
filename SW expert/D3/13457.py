T = int(input())
count = 0
count1 = 0
ans = ''
for i in range(T):
    lst = list(input())

    count = lst.count('x')
    count1 = lst.count('o')
    # print(count, count1)
    if count1 >= 8:
       ans = 'YES'
    elif count <8: 
        ans = 'YES'
    else:
        ans= 'NO'
    print('#{} {}'.format(i+1,ans))