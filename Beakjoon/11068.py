def convertBase(x,B):
    len = 0
    copyX = x
    while copyX>0:
        copyX/=B;
        len+=1
    digit = []
    len=0
    while x>0:
        digit[len+=1] = x%B
        x=x/B
    return digit


T = int(input())
while T>0:  
    ans = False
    for i in range(2,65):
        digit = convertBase(x,i)
        if(isPalindrome(digit)):
            ans = True
        