
n, k = map(int, input().split())

ans = n
while True:
    c = n//k
    ans += c
    n = c + n%k
    if c == 0:
        ans += c
        print(ans)
        break
    else:
        continue