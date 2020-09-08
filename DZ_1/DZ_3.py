print('Вас приветствует программа по просчету суммы числа в формате: "n + nn + nnn"')
n = int(input("Введите число"))
n1 = int(str(n) + str(n))
n2 = int(str(n) + str(n1))
sum = (n + n1 + n2)
print(f"Сумма чисел {sum}")

