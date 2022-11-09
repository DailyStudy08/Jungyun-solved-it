queue1 = [1,2,1,2]
queue2 = [1,10,1,2]

def solution(queue1, queue2):
    onesum = sum(queue1)  #각 큐의 합을 저장한다.
    twosum = sum(queue2)
    for i in range (300000):  #최대 300,000번만 가능
        if onesum == twosum:  #같은 순간 정답인 i값 출력
            return i
        elif onesum>twosum:  #onesum이 더 크면
            value = queue1.pop(0)  #queue1 값을 빼서
            queue2.append(value)  #queue2에 추가
            onesum -= value  #합 또한 맞게 바꿔준다.
            twosum += value
            # print(queue1,queue2)  #디버깅
        else: 
            value = queue2.pop(0)  #twosum이 더 크면
            queue1.append(value)  #변수끼리 바꿔서 그대로
            onesum += value
            twosum -= value
            # print(queue1,queue2)  #디버깅
    return -1  # 같은 적이 없다면 -1

# print(solution(queue1, queue2))  #프로그래머스에선 필요없
