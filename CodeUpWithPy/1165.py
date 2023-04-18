time,goal = map(int,input().split())
c = int((90-time)//5)

if time%5 ==0:
    print(goal+c)
else:
    print(goal+c+1)
