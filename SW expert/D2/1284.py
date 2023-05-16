T = int(input())
A = 0
B = 0
for i in range(0,T):
    P,Q,R,S,W = map(int , input().split())
    # print(P,Q,R,S,W)
    A = P*W
    if W>R:
        B= Q+(W-R)*S
    else:
        B= Q
    print(A,B)
    # print('#{} {}'.format(i+1,min(A,B)))
   