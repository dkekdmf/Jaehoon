import sys
def bubblesort(data):
    global swap
    for index in range(len(data)-1):
        for index2 in range(len(data)-index-1):
            if data[index2] > data[index2+1]:
                data[index2],data[index2+1] = data[index2+1],data[index2]
                swap +=1
       

N = int(input())
swap = 0
lst = list(map(int,sys.stdin.readline().split()))
bubblesort(lst)
print(swap)