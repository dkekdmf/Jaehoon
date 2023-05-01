a= int(input())
b= list(input())
# c= []
count =0
count1 = 0
for i in range(a):
    if b[i] =='A':
        count+=1
    elif b[i] == 'B':
        count1+=1
if count>count1:
    print('A')
elif count<count1:
    print('B')
else:
    print('Tie')

        

