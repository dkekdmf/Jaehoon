B = int(input(),16)

for i in range(1,16):
    print('%X'%B,'*%X'%i,'=%X'%(B*i),sep= '')