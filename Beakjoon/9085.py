T = int(input())

for i in range(T):
    a = int(input())
    lst = list(map(int,input().split()))
    sum = 0
    for i in lst:
        sum+=i
    print(sum)
    #sum1 = sum(lst)
    # print(sum1)