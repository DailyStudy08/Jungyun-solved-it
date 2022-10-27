n = int(input())

team_point= [ ]

start = []
link = []
for _ in range(n):
    team_point.append(list(map(int,input().split())))

def dfs(idx):
    global minans

    if idx == n //2:
        start_team =0
        link_team = 0
        for i in range(0,n):
            if i not in start:
                link.append(i)
        for i in range(0,n//2-1):
            for j in range(i+1,n//2):
                start_team += team_point[start[i]][start[j]]+team_point[start[j]][start[i]]
                link_team +=team_point[link[i]][link[j]]+team_point[link[j]][link[i]]
        diff =abs(start_team-link_team)

        if minans >diff:
            minans =diff
        link.clear()
        return

    for i in range(n):
        if i in start:
            continue
        if len(start) >0 and start[len(start)-1] > i:
            continue
        start.append(i)
        dfs(idx +1)
        start.pop()

minans = float('Inf')
dfs(0)
print(minans)