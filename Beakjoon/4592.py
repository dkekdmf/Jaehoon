
while True:
    ans = []
    a= input().split()
    print(type(a))
    if a[0]=='0':
        break
    a.remove(a[0])
    for i in a:
        if len(ans) ==0:
            ans.append(i)
        elif ans[-1]!=i:
            ans.append(i)
    ans.append('$')
    # print(' '.join(ans))
       

    