
while True:
    a= input()
    if a== '0':
        break
    if a[0:] == a[len(a): :-1]:
        print('yes')
    else:
        print('no')