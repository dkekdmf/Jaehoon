a= int(input())
b= int(input())

if 2<a:
    print('After')
elif a<2:
    print('Before') 
elif a==2:
    if b<18:
        print('Before') 
    elif b==18:
        print('Special')
    else:
        print('After')
         
        