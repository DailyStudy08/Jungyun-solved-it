n, w, h, l = map(int, input().split())
cow = (w // l) * (h // l)
if n < ans:
    print(n)
else:
    print(cow)