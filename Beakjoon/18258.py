import sys
from collections import deque

N= int(sys.stdin.readline())
queue =  deque([])
for _ in range(N):
   cmd = list(input().split())
 
   if cmd[0] == "push":
       queue.append(cmd[1])
   elif cmd[0] == "pop":
       if len(queue) == 0:
           print(-1)
       else:
          data = queue[0]
          del queue[0]
          print(data)
   elif cmd[0] == "size":
      print(len(queue))
   elif cmd[0] == "empty":
       if len(queue) == 0:
           print(1)
       else:
           print(0)
   elif cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
   elif cmd[0] == "back":
         if len(queue) == 0:
                print(-1)
         else:
            print(queue[-1])