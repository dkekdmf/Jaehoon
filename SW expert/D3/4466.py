T = int(input())

for i in range(T):
    a,b = map(int,input().split())
    lst = list(map(int , input().split()))
    # print(a,b,lst)

    # lst.sort(reverse=True)
    for i in range(a-1):
           for j in range(i+1,a):
              if lst[i]< lst[j]:
                lst[i],lst[j] = lst[j],lst[i]    
         
    sum = 0
    for i in range(b):
        sum+=lst[i]  
    print('#{} {}'.format(i+1,sum))
# for testcase in range(1,T+1):
#     a, b = map(int, input().split())
#     arr = list(map(int, input().split()))
#     for i in range(a-1):
#         for j in range(i+1,a):
#             if arr[i]< arr[j]:
#                 arr[i],arr[j] = arr[j],arr[i]
#     total = 0
#     for i in range(b):
#         total +=arr[i]

#     print(f'#{testcase} {total}')
