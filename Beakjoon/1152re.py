a= list(input().split(' '))
print(a)
count =0

print(len(a))
for i in a:
    count+=1
    if (a[0] ==""):
        a.pop(0)
    elif a[-1] =="":
        a.pop(-1)
print(count)
    