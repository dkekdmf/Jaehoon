N = int(input())

for i in range(N):
    a = input()
    if a=='P=NP':
        print('skipped')
    else:
        n,m = map(int,a.split('+'))
        print(n+m)
   