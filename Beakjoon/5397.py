T = int(input())

for _ in range(T):
    leftstack = []
    rightstack = []
    data1 = input()
    
    for i in data1:
        if i =='-':
            if leftstack:
                leftstack.pop()
        elif i== '<':
            if leftstack:
                rightstack.append(leftstack.pop())
        elif i =='>':
            if rightstack:
                leftstack.append(rightstack.pop())
        else:
            leftstack.append(i)
    leftstack.extend(reversed(rightstack))
    print(''.join(leftstack))