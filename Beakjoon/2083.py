while True:
     name,age,weight = input().split()
     age = int(age)
     weight = int(weight)
     if '#' in name:
        break
     if age>17 or weight>=80:
            ans = 'Senior'
     else:
            ans = 'Junior'
            
     print('{} {}'.format(name,ans))