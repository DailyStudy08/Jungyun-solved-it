T = int(input())

for i in range(T):
    N = int(input())
    net_C = 0
    net_G = 0
    
    for j in range(N):
        C, G = map(float, input().split())
        net_C += C
        net_G += C * G
        
    GPA = net_G / net_C
    print(f'{int(net_C)} {GPA}')