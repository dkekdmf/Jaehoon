a = int(input())

count1 = 1
stack1 = []
result1 = []

for i in range(1,n+1):
    data1 = int(input())
    while count1<=data:
        stack1.append(count1)
        count1+=1
        result1.append('+')
    if stack1[-1] == data1:
        stack1.pop()
        result1.append('-')
    else:
        print('NO')
        exit(0)
print('\n'.join(result1))