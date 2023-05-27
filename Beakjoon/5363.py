N = int(input())

for i in range(N):
    a = input().split()
    b  = a[0]
    c = a[1]
    a.remove(a[0])
    a.remove(a[0])
    a.append(b)
    a.append(c)
    print(" ".join(a))

    
    


