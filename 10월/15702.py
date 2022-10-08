N, M = map(int,input().split())
baejum = list(map(int,input().split()))

student = list(map(str,input().split()))
num = student.pop(0)
score = 0
bestudent = []
highest = []
for i in range (len(student)):
    if student[i] == 'O':
        score += baejum[i]
    else:
        pass
highest.append(score)
bestudent.append(num)

for tc in range (1, M):
    student = list(map(str,input().split()))
    #print(student)
    num = student.pop(0)
    score = 0
    for i in range (len(student)):
        if student[i] == 'O':
            score += baejum[i]
        else:
            pass
    if highest[0] < score:
        highest.pop(0)
        highest.append(score)
        bestudent = []
        bestudent.append(num)
    elif highest[0] == score:
        bestudent.append(num)
    else:
        pass
    bestudent = sorted(bestudent)

print(f'{bestudent[0]} {highest[0]}')