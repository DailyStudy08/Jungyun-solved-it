a=int(input())
b=int(input())
c=int(input())
num=a*b*c
cnt=[0]*10
while num>0:
    cnt[num%10]+=1
    num=num//10
for i in cnt:
    print(i)