year,month,day = map(int,input().split())

if (year-month+day)%10==0:
    print("대박")
else:
    print("그럭저럭")