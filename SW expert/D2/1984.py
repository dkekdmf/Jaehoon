a= int(input())

for i in range(a):
          lst = list(map(int, input().split()))
          lst.remove(max(lst))
          lst.remove(min(lst))
       
          print(f'#{i+1} {round(sum(lst)/8)}')
    
    