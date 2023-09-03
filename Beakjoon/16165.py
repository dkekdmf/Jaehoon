A,B = map(int, input().split())

team_mem, mem_team = {},{}

for i in range(A):
    team_name1,mem_num1 = input(), int(input())
    team_mem[team_name1]= []
    for j in range(mem_num1):
        name = input()
        team_mem[team_name1].append(name)
        mem_team[name] = team_name1
for i in range(B):
    name,q = input(),int(input())
    if q:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)
            