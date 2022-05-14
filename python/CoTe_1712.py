# 백준 1712번 손익분기점 --> for문이 아닌 수학적 알고리즘으로 접근. 훨씬 짧고 간결함.

A, B, C = map(int,input().split()) 

if B >= C :
    print(-1)

else :
    print(A//(C-B)+1)
