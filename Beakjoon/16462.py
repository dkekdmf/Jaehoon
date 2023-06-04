import math
N = int(input())
avg = 0.0
for i in range(N):
    
    a= input()
   
    if int(a) == 100:
          avg+=100
    else:
        a = a.replace("0","9")
        a = a.replace("6","9")
        avg+=int(a)
avg = avg/float(N)
print(int(round(avg,2)))
    
    
    