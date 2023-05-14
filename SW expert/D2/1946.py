T = int(input())

for i in range(1,T+1):
    a = int(input())
    value = ""
    for j in range(a):
        b,c = input().split()
        c = int(c)
        value +=b*c
# print(value)
    print('#{}'.format(i))
    for i in range(len(value)):
         if (i+1)%10 ==0:
            print(value[i])
         else:
            print(value[i],end = '')
    print()