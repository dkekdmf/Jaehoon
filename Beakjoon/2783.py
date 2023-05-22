X,Y = map(int, input().split())
N = int(input()) # N이 int(input())일때는 배열에 그냥 접근 len쓰면 오류남.
mul = X*1000/Y
for i in range(N):
    a,b = map(int,input().split())
    # print(a,b)
    # print(a*b) #print(a*b)하면, 첫재줄 부터 마지막줄까지 차례대로 곱함.
    mul = min(mul,a*1000/b)
print(round(mul,2))
    
    