n = input().split()
r= n[0][0]
rem = ['i','pa','te','ni','niti','a','ali','nego','no','ili']

for i in range(1,len(n)):
    if n[i] in rem:
        continue
    else:
        r+=n[i][0]
    print(r.upper())
    

