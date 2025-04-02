N,M = map(int,input().split())
arr = []
for _ in range(N):
    data = input()
    arr.append(data)
       
def isExist(lst,x):
        l,r = 0,len(lst)-1
        while l<=r:
          m = (l+r)//2
          if x==lst[m]: 
            return True  
            break
          elif x>=lst[m]:
            l = m+1
          elif x<=lst[m]:
            r = m-1
        return False
count = 0
arr.sort()
while M>0:
    x = input()
    if(isExist(arr,x)):
        count+=1
    M-=1
print(count)
        