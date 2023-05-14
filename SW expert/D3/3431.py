T = int(input())
ans = 0
for i in range(T):
    a,b,c = map(int, input().split())
    if c<a:
        ans = a-c
    elif a<c<b:
        ans = '0'
    elif c>b:
        ans = '-1'
    print('#{} {}'.format(i+1,ans))
# a= [list(map(int,input().split())) for i in range(3)]
# # print(a[1][2])
# print(len(a))
# for i in range(1):
#     print()
#     if a[i] < a[i-2]:
#         print(a[i-2]- a[i])
#     elif a[i-2]<a[i]<a[i-1]:
#         print('0')
#     elif a[i]>a[i-2]:
#         print('-1')
#     # if a[2]<a[0]:
   
# #     print(a[0]-a[2])
# # elif a[0]<a[2]<a[1]:
# #     print('0')
# # elif a[2]>a[1]:
# #     print('-1')