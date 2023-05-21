while True:

    a= input()
    res = len(a)+1
    if a =='0':
        break;
    for n in a:
      if n=='1':
         res+=2
      elif n=='0':
         res+=4
      else:
          res+=3
    print(res)