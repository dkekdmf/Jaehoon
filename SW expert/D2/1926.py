

# for i in range(N):
#     if i%10 ==3 or i%10==6 or i%10==9:
#         print('-')
#     elif i//10==3 or i//10==6 or i//10==9:
#         print('--')
#     else:
#         print(i)
N= int(input())
for i in range(1,N+1):
    i = str(i)
    clap = i.count('3') + i.count('6')+ i.count('9')
  
    if clap == 0:
        print(i,end= ' ')
    else:
        print('-'*clap,end = ' ')
        
T = int(input())
for i in range(1, T+1): # 1 ~ 100

    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end=' ')