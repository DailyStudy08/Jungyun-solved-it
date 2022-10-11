from sys import stdin

input = stdin.readline

board = [list(map(int, list(input().strip()))) for _ in range(8)]
used = [[False]*7 for _ in range(7)]
visited = [[False]*7 for _ in range(8)]

def solv():
    print(go(0,0))

def go(x,y):
    global used,visited
    if x == 8:
        return 1
    count = 0
    nnx = x
    nny = y + 1
    if nny == 7:
        nnx = x + 1
        nny = 0
    if visited[x][y]:
        return go(nnx,nny)
    else:
        now = board[x][y]
        visited[x][y] = True
        for dx,dy in ((0,1),(1,0)):
            nx = x + dx
            ny = y + dy

            if boundray_validator(nx,ny):
                nxt = board[nx][ny]

                if not used[now][nxt] and not visited[nx][ny]:
                    used[now][nxt] = used[nxt][now] = True
                    visited[nx][ny] = True
                    count += go(nnx,nny)
                    visited[nx][ny] = False
                    used[now][nxt] = used[nxt][now] = False
        visited[x][y] = False
        return count

def boundray_validator(x,y):
    if x >= 8 or y >= 7:
        return False
    return True
solv()