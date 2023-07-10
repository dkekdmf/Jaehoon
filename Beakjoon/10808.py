S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in S:
        print(1)
    else:
        print(0)
        
arr=input()
cnt=[0]*26

for i in arr:
    cnt[ord(i)-97]+=1

print(*cnt)