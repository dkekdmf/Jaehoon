N = int(input())
for i in range(N):
    lst= list(input())
    for i in lst:
        lst[0] = lst[0].upper()
    result = ''.join(lst)
    print(result)