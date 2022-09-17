N = int(input())
data = list(input())
aski = []
cnt = 1
for i in range (N):
    aski.append(ord(data[i]))
#print(aski)
result = 'NO'
for i in range (1,N):
    while True:       
        if aski[i] +1 == aski[i-1] or aski[i] -1 == aski[i-1]:
            cnt += 1
            if cnt == 5:
                result = 'YES'
                break
        else:
            cnt = 1   
        break
print(result)