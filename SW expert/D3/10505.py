T = int(input())
lst=[]

for i in range(T):
    a = int(input())
    b= list(map(int , input().split()))

    sum1 = sum(b)
    avg = sum1//a

    count = 0
    for s in b:
        if int(s) <= avg:
            count+=1
    print('#{} {}'.format(i+1,count))
