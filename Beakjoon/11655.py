lst= input()
ans = ''   
for i in lst:
    if i>='a' and i<='z':
       i = ord(i)+13
       if i>122:
           i-=26
       ans+=chr(i)
    elif i>='A' and i<='Z':
        i = ord(i)+13
        if i>90:
             i-=26
        ans+=chr(i)
    else:
        ans+=i
print(ans)