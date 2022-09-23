n = int(input())
def pibo(a):
    if a == 0:
        return 0
    num = [1,1]
    if a == 1:
        return num[0]
    elif a == 2:
        return num[1]
    else:
        k = a-2
        for i in range (k):
            num.append(num[0]+num[1])
            num.pop(0)
        return num[1]
print(pibo(n))