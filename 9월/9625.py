'''
screen = ['A']
n = int(input())
for i in range (n):
    
    for j in range (len(screen)):
        if screen[0] == 'A':
            screen.pop(0)
            screen.append('B')
        elif screen[0] == 'B':
            screen.pop(0)
            screen.append('B')
            screen.append('A')
#print(screen)
a_cnt = 0
b_cnt = 0
for i in screen:
    if i == 'A':
        a_cnt += 1
    if i == 'B':
        b_cnt += 1
print(f'{a_cnt} {b_cnt}')
'''
a = int(input())
arr = [0, 1]
if a == 1:
    pass
elif a == 2:
    arr.pop(0)
    arr.append(2)
else :
    k = a-3
    arr = [1,2]
    for j in range (k):
        arr.append(arr[0]+arr[1])
        arr.pop(0)
print(arr[0], arr[1])

