a = int(input())
def pibo(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(1)
    else:
        return pibo(n-2) + pibo(n-1)
print(pibo(a))