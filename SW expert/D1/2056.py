T = int(input())

for i in range(T):
    lst = str(input())
    days = {1:31,2:28,3:31,4:30,5:31,6:30,
        7:31,8:31,9:30,10:31,11:30,12:31}
    year = lst[:4]
    month = lst[4:6]
    day = lst[6:]
    fail = -1
    if 0<int(month)<13 and int(day) <= days[int(month)]:
        print('#{} {}/{}/{}'.format(i+1,year,month,day))
    else:
        print('#{} {}'.format(i+1,fail))  

   