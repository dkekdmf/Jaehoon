lst = list(map(int , input().split()))
count = {}
max = 0
mode =0
for i in lst:
   try: count[i]+=1
   except:count[i]=1

for key,value in count.items():
    if value > max:
        max =value
        mode = key
    elif max == value:
        if mode<key:
            mode = key
print(count,lst,mode,max)


    
    
#for 문 돌리면서 가장 많이 나온값 count ++ 