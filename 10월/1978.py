N = int(input())  #입력
k = list(map(int,input().split()))

cnt = 0  #정답

for i in range (N):
    if k[i] == 1:  #1이면 통과
        pass
    else:
        c = 2  #2부터 비교 시작
        while c < k[i]:  #c가 k[i]보다 작다는 전제하에
            if k[i]%c == 0:  #나눠지면 소수가 아님
                break  #끝
            else:
                c += 1  #계속 더하다가
                if c == k[i]:  #두개가 같으면
                    cnt += 1  #소수다!
                    break

print(cnt)  #출력