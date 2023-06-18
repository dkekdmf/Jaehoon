a = list(input())

for i in a:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    print(i,end = '')