N = int(input())
num = list(map, int,input().split())
ans = []

for i in range (N):
    ans.insert(i-num[i], i+1)

for k in ans:
    print(k, end='')