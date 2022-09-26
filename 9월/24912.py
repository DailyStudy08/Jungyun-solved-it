N=int(input())
Cards=list(map(int,input().split()))

if N==1:
    if Cards[0]==0:
        print(1)
    else:
        print(Cards[0])
    sys.exit()

for i in range(N):
    if Cards[i]==0:
        if i==0:
            num=0
            for j in range(1,4):
                if Cards[1]!=j:
                    num=j
                    break
            Cards[0]=num
        elif i==(N-1):
            num=0
            for j in range(1,4):
                if Cards[N-2]!=j:
                    num=j
                    break
            Cards[N-1]=num
        else:
            num=0
            for j in range(1,4):
                if j not in [Cards[i-1],Cards[i+1]]:
                    num=j
                    break
            Cards[i]=num

    if i>0 and Cards[i-1]==Cards[i]:
        print(-1)
        sys.exit()

print(" ".join(map(str,Cards)))