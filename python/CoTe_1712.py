# 백준 1712번 손익분기점

A, B, C = map(int,input().split())
result = A + B - C
cnt = 1

while True :    

    if result < 0 :
        break    
    
    elif B > C :
        print(-1)
        break

    result = result + B - C
    cnt += 1

if B < C :
    print(cnt)
