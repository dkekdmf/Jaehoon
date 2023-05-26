sum =0
count = [0] * (1000 + 1)
for i in range(10):
 
   a = int(input())
#    print(a)
   sum+=a
   count[a]+=1
print(sum//10)
print(count.index(max(count)))

