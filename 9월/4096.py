
def solution() :
    while 1 :
        n = sys.stdin.readline().rstrip()
        count = 0
        if n == '0' :
            break
        elif n == n[::-1] :
            print(count)
            continue
        else :
            tmp = len(n)
            while n != n[::-1] :
                count += 1
                t = int(n) + 1
                n = str(t).zfill(tmp)
            print(count)
            continue
                
solution()