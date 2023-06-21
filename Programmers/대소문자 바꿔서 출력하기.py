str  = input()
print(str)
for i in str:
    if i.isupper():
     i = i.lower()
    else:
     i = i.upper()
    print(i,end ="")
