hogu = 0
while True:
    money = int(input())
    hogu += money
    if money == -1:
        hogu += 1
        break
print(hogu)
