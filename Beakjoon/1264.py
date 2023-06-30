M = ['a','e','i','o','u','A','E','I','O','U']

while True:
    count = 0
    a = input()
    if a =='#':
        break
    for item in a:
        if item in M:
            count+=1
    print(count)