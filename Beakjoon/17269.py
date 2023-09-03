N,M = map(int , input().split())
A,B = input().split()

alphabet = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]



res = ''
minlen = min(N,M)
for i in range(minlen):
    res += A[i] + B[i]
res += A[minlen:] + B[minlen:]

lst1 = [alphabet[ord(i)-ord('A')] for i in res]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst1[j] += lst1[j+1]
print("{}%".format(lst1[0]%10*10+lst1[1] % 10))