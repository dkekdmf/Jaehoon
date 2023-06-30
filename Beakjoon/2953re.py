lst = [sum(list(map(int,input().split()))) for i in range(5)]

print(lst.index(max(lst))+1,max(lst))