S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in S:
        print(S.index(i))
    else:
        print(-1)