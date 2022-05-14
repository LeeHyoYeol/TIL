# 백준 2292번 벌집

target = int(input())

seqNum = 1
loopcnt = 1

while target > seqNum :

    seqNum = seqNum + loopcnt * 6
    loopcnt += 1

print(loopcnt)
