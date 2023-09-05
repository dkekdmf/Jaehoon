current = input()
drop = input()

currentUnit = current.split(":")
currentHour = int(currentUnit[0])
currentMinute = int(currentUnit[1])
currentSecond = int(currentUnit[2])

currentSecondAmount = currentHour*3600+currentMinute*60+currentSecond
dropUnit = drop.split(":")
dropHour = int(dropUnit[0])
dropMinute = int(dropUnit[1])
dropSecond = int(dropUnit[2])
dropSecondAmount = dropHour*3600+dropMinute*60+dropSecond

needSecondAmount = dropSecondAmount-currentSecondAmount

if needSecondAmount<=0:
    needSecondAmount+=24*3600
needHour = needSecondAmount/3600
needMinute = (needSecondAmount%3600)/60
needSecond = needSecondAmount%60

print("%02d:%02d:%02d" %(needHour,needMinute,needSecond),end='')
