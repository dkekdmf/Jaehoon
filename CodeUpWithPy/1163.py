year,month,day = map(int, input().split())
if ((year+month+day)//100)%2==0:
    print("대박")
elif ((year+month+day)//100)%2==1:
    print("그럭저럭")