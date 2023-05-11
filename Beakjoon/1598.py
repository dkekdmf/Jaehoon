a,b = map(int,input().split())

a -=1;
b-=1
c = abs(b//4 - a//4)
d = abs(b%4 - a%4)
print(c+d)
