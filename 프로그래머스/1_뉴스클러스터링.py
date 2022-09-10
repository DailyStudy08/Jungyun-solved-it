def solution(str1, str2):
    answer = 0
    list1 = []
    list2 = []
    #list로 쪼개서 받기
    for i in range (len(str1)-1):
        list1.append(str1[i:i+2])
    for i in range (len(str2)-1):
        list2.append(str2[i:i+2])
    #문자열만 남기기
    lista = []
    listb = []
    for i in list1:
        if i.isalpha() == True:
            i = i.lower()
            lista.append(i)
    for i in list2:
        if i.isalpha() == True:
            i = i.lower()
            listb.append(i)
    #교집합
    a = lista.copy()
    b = listb.copy() #나중에 copy지우고 진행한 결과 보여주자.
    gyo = []
    for i in a:
        if i in b:
            b.remove(i)
            gyo.append(i)
    print(gyo)
    #합집합
    hap = []
    for i in lista:
        hap.append(i)
    for i in listb:
        hap.append(i)
    for i in gyo:
        hap.remove(i)
    print(hap)
    #임시 답 구하기
    temp = 0
    while True:
        if len(hap) == 0:
            temp = 1
            break
        elif len(gyo) == 0:
            temp = 0
            break
        else:
            temp = (len(gyo)/len(hap))
            break
    answer = int(temp * 65536)
    return answer