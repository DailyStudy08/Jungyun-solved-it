N = int(input())
company = []
for n in range (N):
    k = input().split(' ')
    if k[1] == 'enter':
        company.append(k[0])
    elif k[1] == 'leave':
        try:
            company.remove(k[0])
        except:
            pass
company = sorted(company, reverse=True)
print(' '.join(company))

n = int(input)

people = {}

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        people[name]
    elif status == 'leave':
        del(people[name])
for name in sorted(people.keys(), reverse = True):
    print(name)