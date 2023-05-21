T = int(input())

for k in range(T):
    even = []
    lst = list(map(int, input().split()))
    for i in lst:
        if i %2 == 0:
            even.append(i)
    print(sum(even))
    print(min(even))
    
    
    
    
    #      if lst[i]%2 ==0:
    #       sum += lst[i]
    #      if min>lst[i]:
    #       min = lst[i]
    
    # print(sum)
    # print(min)

           
        