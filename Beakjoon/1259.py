while True:
    p = input()
    if p=='0':
        break
    print(p)
    if p[0:] == p[-1: : -1]:
        print('yes')
    else:
        print('no')
        
while True:
    a= input()
    if a== '0':
        break
    if a[0:] == a[len(a): :-1]:
        print('yes')
    else:
        print('no')
        
while True:
    p = input()
    if p=='0':
        break

    if p[0:] == p[len(p): : -1]:
        print('yes')
    else:
        print('no')