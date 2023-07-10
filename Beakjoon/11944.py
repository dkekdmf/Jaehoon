from sys import stdin
n,m = map(int,stdin.readline.split())
if len(str(n)*n) >m:
    print(str(n)*n[:m])
else:
    print(str(n)*n)