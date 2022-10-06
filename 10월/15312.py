#알파벳을 숫자로!
a_to_i = {'A':3,'B':2,'C':1,'D':2,'E':3,'F':3,'G':2,
'H':3,'I':3,'J':2,'K':2,'L':1,'N':2,'M':2,'O':1,'P':2,
'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}

A = list(input())  #입력부
#print(A)
B = list(input())
#print(B)

C = []  #비어있는 리스트

for i in range (len(A)):  #A와 B를 합친다
    C.append(A[i])
    C.append(B[i])
#print(C)
for i in range (len(C)):
    C[i] = a_to_i[C[i]]
#print(C)

D = []  #또다른 비어있는 리스트
while True:  #일단 돌린다.
    for i in range(len(C)-1):
        if C[i]+C[i+1] >= 10:  #두개의 합이 10보다 크면
            D.append(C[i]+C[i+1]-10)  #10빼고 진행
        else:  #아니면
            D.append(C[i]+C[i+1])  #그대로
    #print(D)

    if len(D) == 2:  #만약 길이가 2면
        print(f'{D[0]}{D[1]}')  #2개 출력
        break  #끝
    else:  #아니라면
        C = []  #비워놓고 받을 준비

    for i in range(len(D)-1):  #위의 과정을 C를 D로 D를 C로 넣고 반복
        if D[i]+D[i+1] >= 10:
            C.append(D[i]+D[i+1]-10)
        else:
            C.append(D[i]+D[i+1])
    #print(C)
    if len(C) == 2:
        print(f'{C[0]}{C[1]}')
        break
    else:
        D = []