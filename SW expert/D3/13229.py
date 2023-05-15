day = {"MON":1,"TUE":2,"WED":3,"THU":4,"FRI":5,"SAT":6,"SUN":0}
# print(day)
days = {}
T = int(input())
ans = 0
for i in range(T):
    a = input()
    for key,value in day.items():
        if (key == a):
             ans = 7-value
    print('#{} {}'.format(i+1,ans))
        
            
                   
            
             
     
       


    