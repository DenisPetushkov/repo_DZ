n = abs(int(input("Введите положительное целое число")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print(f"Максимальная цифра в числе: {max}")
        break
