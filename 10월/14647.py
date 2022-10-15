N, M = map(int,input().split())  #입력

bingo = [list(map(str,input().split())) for _ in range (N)]

#print(bingo)

ans = 0

for i in range (N):  #가로방향순회
    cnt = 0
    for j in range(M):
        for k in range (len(bingo[i][j])):
            if bingo[i][j][k] == '9':
                cnt += 1
    # print(cnt)
    if cnt >= ans:
        ans = cnt

for i in range (M):  #세로방향순회
    cnt = 0
    for j in range(N):
        for k in range (len(bingo[j][i])):
            if bingo[j][i][k] == '9':
                cnt += 1
    # print(cnt)
    if cnt >= ans:
        ans = cnt


print(ans)  #출력