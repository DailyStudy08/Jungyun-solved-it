a = list(input())
c = input()
b = []
for i in range (len(a)):
    if a[i].isalpha() == True:
        b.append(a[i])
    else:
        pass

d = ''.join(b)

if c in d:
    print(1)
else:
    print(0)