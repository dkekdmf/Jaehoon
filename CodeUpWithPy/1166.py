a = int(input())

if a%400 == 0:
    print("Leap")
elif a%4==0 and a%100!=0:
    print("Leap")
else:
    print("Normal")