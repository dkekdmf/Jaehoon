X,Y = map(str,input().split())

result = str(int(X[::-1])+ int(Y[::-1]))
print(int(result[::-1]))