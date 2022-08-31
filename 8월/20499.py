'''
k,d,a = map(int,input().split('/'))
if k+a < d:
    print('hasu')
else:
    if d == 0:
        print('hasu')
    else:
        print('gosu')
'''
k,d,a = map(int,input().split('/'))
print(k,d,a)
if k+a < d or d==0:
    print('hasu')
else:
    print('gosu')