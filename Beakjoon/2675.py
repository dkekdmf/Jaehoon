a = int(input())


for i in range(a):
    s,b = input().split()
    text = ''
    for i in b:
        text +=int(s)*i
    print(text)