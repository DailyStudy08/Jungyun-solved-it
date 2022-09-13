#입력값 다 받아버리기
line, num = map(int, input().split())
alzip = [list(input()) for _ in range (line)]
solve = [list(input()) for _ in range (line)]
unzip = []
temp = []
#alzip 길이 두배로 확장
for i in range (line):
    for j in range (num):
        unzip.append(alzip[i][j])
        unzip.append(alzip[i][j])
#solve에 있는 거 꺼내오기
for i in range (line):
    for j in range (num*2):
        temp.append(solve[i][j])
# print(solve)
# print(unzip)
# print(temp)
# 답 비교하기
ans = 'Eyfa'
for i in range (num*2):
    if unzip[i] == temp[i]:
        pass
    else:
        ans = 'Not Eyfa'
print(ans)
'''
n,m = map(int,input().split())

A = ["".join([i*2 for i in input().rstrip()]) for _ in range(n)]
B = ["".join(input().rstrip()) for _ in range(n)]
    
print('Eyfa' if A==B else 'Not Eyfa')
'''