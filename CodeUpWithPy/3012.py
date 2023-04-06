
a= int(input())
stack = []
for _ in range(a):
   cmd = input().strip().split()
   if cmd[0] =="push(":
       stack.append(cmd[1])
   elif cmd[0]=="top()":
       print(stack[-1] if stack else -1)  
   elif cmd[0]=="pop()":
       if stack: stack.pop()
   elif cmd[0] =="size()":
       print(len(stack))
   elif cmd[0] =="empty()":
       print("false" if stack else "true") 
   