N = int(input())
company = []
for n in range (N):
    k = input().split(' ')
    if k[1] == 'enter':
        company.append(k[0])
    else:
        try:
            company.remove(k[0])
        except:
            pass
company = sorted(company, reverse=True)
print(company)