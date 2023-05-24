while True:
    a = input()
   
    if a[0]=='#':
        break
    value = a[0]
    data = a[2:]
    X = data.count(value) + data.count(value.upper())
    print(value, X)
    