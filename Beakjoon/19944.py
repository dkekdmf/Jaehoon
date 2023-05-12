N,M = map(int,input().split())

if M==1 or M==2:
    print('NEWBIE!')
elif M<=N and not (M==1 or M==2):
    print('OLDBIE!')
else:
    print('TLE!')