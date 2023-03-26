h,b,c,s = map(int, input().split())
a= h*c*s*b/8/1024/1024
a= float(a)
print(format(a,".1f"),'MB')

