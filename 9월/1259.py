while True:
    N = list(input())
    if N == ['0']:
        break
    else:
        for i in range (len(N)):
            if N[i] != N[len(N)-i-1]:
                print('no')
                break
            elif i == (len(N)//2) + 1:
                print('yes')
                break
            

