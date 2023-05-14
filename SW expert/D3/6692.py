T = int(input())

for i in range(T):
    a= int(input())
    ans = 0
    
    for _ in range(a):
        b = input().split()
  
        p = float(b[0])
        q = float(b[1])
        ans += p*q
    f= format(ans,".6f")
    print('#{} {}'.format(i+1,f))