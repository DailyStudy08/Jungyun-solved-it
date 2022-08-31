치킨 = int(input())
콜라, 맥주 = map(int, input().split())

음료 = (콜라//2) + 맥주

if 치킨 > 음료:
    print(음료)
else:
    print(치킨)