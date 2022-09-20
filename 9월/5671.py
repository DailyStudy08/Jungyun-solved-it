N, M = map(int, input().split())
hosu = []
for i in range (N, M+1):
    hosu.append(list(str(i)))
#print(hosu)

for i in range (len(hosu)):
    temp = []
    for j in hosu[i]:
        if j in temp:
            pass
        else:
            temp.append(j)
    if len(temp) != len(hosu[i]):
        hosu[i] = []
#print(hosu)
cnt = 0
for i in range (len(hosu)):
    if hosu[i] != []:
        cnt += 1
print(cnt)