a, b = map(int, input().split())
c = int(input())
print(a+b if c*2 > a+b else (a+b)-(c*2))