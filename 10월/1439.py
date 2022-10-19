data = input()  #입력부
change0 = 0
change1 = 0
 

if data[0] == '0':  #0인 경우
    change1 += 1  #1로 바꾸는 경우
else:  # 첫번째가 1 
    change0 += 1  #0으로 바꾸는 경우
    
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            change0 += 1  #0으로 바꾸는 경우
        else:
            change1 += 1  # 1로 바꾸는 경우
            
print(min(change0, change1))  #출력부