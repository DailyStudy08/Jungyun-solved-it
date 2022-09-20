W = list(map(int,input().split()))
S = list(map(int,input().split()))
W_score = 0
S_score = 0
result = 'No'
for i in range (9):
    W_score += W[i]
    if W_score > S_score:
        result = 'Yes'
        break
    S_score += S[i]
print(result)