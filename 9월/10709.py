H, W = map(int, input().split())
sky = [input() for _ in range(H)]
result_sky = [[-1] * W for _ in range(H)]
visited = [[False] * W for _ in range(H)]
cnt = 1
 
def check_cloud():    # 구름이 있는지 없는지 판단하는 함수
    for i in sky:
        if 'c' in i:
            return True
    return False
 
def print_arr(arr):    # arr을 출력하는 함수
    for i in arr:
        print(*i, end=' ')
        print()
 
def visited_cloud():    # 구름의 초기값을 visited하는 함수
    for i in range(H):
        for j in range(W):
            if sky[i][j] == 'c':
                visited[i][j] = True
                result_sky[i][j] = 0
 
if not check_cloud():    # 구름이 하나도 없는 경우
    print_arr(result_sky)    
 
else:    # 구름이 하나라도 있는 경우
    visited_cloud()
 
    while cnt < W:    # 구름이 움직이는 최대 횟수는 W
        temp_arr = [[-1] * W for _ in range(H)]
 
        for i in range(H):
            for j in range(W-1):
                if sky[i][j] == 'c' and not visited[i][j+1]:
                    temp_arr[i][j+1] = 'c'
                    result_sky[i][j+1] = cnt
 
        sky = temp_arr
        cnt += 1
    print_arr(result_sky)