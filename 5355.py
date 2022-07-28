#화성 갈끄니까아!!!!
# @ = *3, % = *5, # = -7
t = int(input())

for _ in range(t):
    a = list(input().split())
    num = float(a.pop(0))
    for i in range(len(a)):
        if a[i] == '@':
            num *= 3
        elif a[i] == '%':
            num += 5
        elif a[i] == '#':
            num -= 7
    
    print(f'{num}')
