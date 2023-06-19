a = input()
#첫번째 방법
print(a.swapcase())
#두번째 방법
for i in a:
    if i.isupper():
        i = i.lower()
    else:
        i = i.upper()
    print(i,end = '')
