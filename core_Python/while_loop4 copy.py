num = 92032123
total = 0

while num > 0:
    rem = num % 10
    num = num // 10
    total = total * 10 + rem
print(total)
