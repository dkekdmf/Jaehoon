N,K  = map(int, input().split())

number = []
count = 0
for i in range(1,N+1):
   
    if N%i ==0:
        number.append(i)
        count+=1
if count<K:
        print('0')
        exit(0)    

print(number[K-1])