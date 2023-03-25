N = int(input())
sum = 0
for i in range(50):
    sum+=i
    if sum>=N:
         print(i)
         break
    