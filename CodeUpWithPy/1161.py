a,b = map(int, input().split())

if a%2==1:
    c= '홀수'
elif a%2==0:
    c= '짝수'
if b%2==1:
    d = '홀수'
elif b%2==0:
    d = '짝수'
if (a+b)%2==1:
    e = '홀수'
if (a+b)%2==0:
    e = '짝수'
print(c + "+"+d+"="+e)
      
    