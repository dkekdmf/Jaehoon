a,b,c = map(int,input().split())
print(a,b,c)
if (a+b)==c:
    print('{}+{}={}'.format(a,b,c))
if a==(b+c):
    print('{}={}+{}'.format(a,b,c))
elif (a-b)==c:
    print('{}-{}={}'.format(a,b,c))
elif a==(b-c):
    print('{}={}-{}'.format(a,b,c))
elif (a*b)==c:
    print('{}*{}={}'.format(a,b,c))
elif a==(b*c):
    print('{}={}*{}'.format(a,b,c))
elif (a/b)==c:
   print('{}/{}={}'.format(a,b,c))
elif a==(b/c):
   print('{}={}/{}'.format(a,b,c))