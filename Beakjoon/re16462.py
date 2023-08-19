N = int(input())
sum = 0
for i in range(N):
   
    a = input()
    if int(a) == 100:
        sum+=100
    else:
       a=a.replace("0","9")
       a=a.replace("6","9")
       sum+=int(a)
avg = sum/float(N)
print(int(round(avg,2)))
    