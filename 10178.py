T = int(input())
for i in range (T):
    c, v = map(int, input().split())
    n = c//v
    m = c%v
    print(f'You get {n} piece(s) and your dad gets {m} piece(s).')