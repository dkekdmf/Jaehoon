def fibonach(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    return fibonach(n-1)+ fibonach(n-2)
print(fibonach(int(input())))