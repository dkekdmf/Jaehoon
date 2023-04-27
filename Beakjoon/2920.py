N = list(map(int, input().split()))
ascending = True
descending = True
for i in range(0,7):
    if N[i]< N[i+1]:
       descending = False
    elif N[i] >N[i+1]:
       ascending = False

if ascending:
    print('ascending')
elif descending:
    print('desending') 
else:
    print('mixed')  
