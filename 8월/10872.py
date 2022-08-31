n = int(input())

def facto(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return facto(a-1) * a

print(facto(n))