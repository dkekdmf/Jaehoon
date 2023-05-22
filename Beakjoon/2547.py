T = int(input())

for i in range(T):
    
    q = input()
    # print(q)
    N = int(input())
    # print(N)
    lst = [int(input()) for i in range(N)]
    # print(lst)
    sum1 = sum(lst)
    tot = len(lst)
    # print(sum1,tot)
    if sum1%tot ==0:
        print('YES')
    else:
        print('NO')