# sum of all digits
num = 54321
total = 0


while num > 0:
    rem = num % 10
    num = num // 10
    total += rem
    print(rem, num, total)