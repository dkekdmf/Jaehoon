# list = [0 for i in range(26)]
# res = 0

# for ch in input():
#     list[ord(ch) - ord('a')] += 1
# for ch in input():
#     list[ord(ch) - ord('a')] -= 1

# print(sum(map(abs, list)))

lst = [0 for i in range(26)]
ans = 0

for s in input():
    lst[ord(s)- ord('a')] +=1
for s in input():
    lst[ord(s) - ord('a')]-=1
    
print(sum(map(abs,lst)))