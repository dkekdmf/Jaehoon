a,b = map(int,(input().split()))


for i in range(0,b): #T는3 
    for j in range(1,a+1):#1부터 4까지
        print(i+j*a,end = ' ') #3*(0,1,2), + 1 2 3
    print()
    #0일때 1,2,3 --> 1,4,7
    #                2.5.8
    #T = 3           3,6,9
    
# a = int(input())

# for i in range(0,a):
#     for j in range(1,a+1):
#         print(a*i+j,end= ' ')
#     print()
   
