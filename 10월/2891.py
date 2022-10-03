one_line = input()
team_n, team_x  ,team_o = one_line.split()
team_n = int(team_n)
team_x = int(team_x)
team_o = int(team_o)
x_num = []
o_num = []
two_line = input()
two_line_list = list(map(int, two_line.split()))
three_line = input()
three_line_list = list(map(int, three_line.split()))
team = [0 for i in range(team_n)]
for i in two_line_list:
    team[i-1] = -1
for i in three_line_list:
    if team[i-1] == -1:
        team[i-1] = 0
    else:
        team[i-1] = 1
for i in range(len(team)):
    if team[i] == 0:
        continue
    elif team[i] == -1:
        if i>0:
            if team[i-1] == 1:
                team[i]=0
                team[i-1] =0
                continue
        if i<len(team)-1:
            if team[i+1] == 1:
                team[i+1]=0
                team[i]=0
                continue
    else:
        continue
print(team.count(-1))