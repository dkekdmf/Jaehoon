while True:
    a = int(input())
    voca = []
    if a== 0:
        break
    for i in range(a):
        voca.append(input())
        voca.sort(key = str.lower)
    print(voca[0])
       