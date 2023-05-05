# a  = int(input())
# count = 0
# for i in range(1,a):
#     b = list(input())
#     if b[i] >= b[i-1]:
#         count+=1
#     print(count)

n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book]+=1
target = max(books.values())
array = []

for book,number in books.items():
    if number == target:
        array.append(book) 
print(sorted(array)[0])       