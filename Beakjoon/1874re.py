a= int(input())
count = 1
result = []
stack = []

for i in range(1,a+1):
    data = int(input())
    while count<= data:
        stack.append(count)
        count+=1
        result.append('+')
    if stack[-1]== data:
            stack.pop()
            result.append('-')
    else:
            print('NO')
            exit(0)
print('\n'.join(result))