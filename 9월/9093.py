T = int(input())
for t in range (T):
    word = list(input())
    temp = []
    ans = []
    for i in word:
        if i != ' ':
            temp.append(i)
        else:
            for j in range(len(temp)):
                ans.append(temp.pop(-1))
            ans.append(i)
    for i in range(len(temp)):
                ans.append(temp.pop(-1))
    print(''.join(ans))
    