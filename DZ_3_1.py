print("Прогррамма выполнит деление чисел")
def diff(*args):

    try:
        arg_1 = int(input("Введите целое число 1: "))
        arg_2 = int(input("Введите целое число 2: "))
        res = arg_1 / arg_2
    except ValueError:
        return "Ошибка! Value error"
    except ZeroDivisionError:
        return "Ошибка!Wrong devider! You can't use zero as a devider"

    return res

print(f'Результат  {diff()}')

""" Для исключения из ошибки
    try:
        num_1 = int(num_1)
        print(num_1)
    except ValueError:
        print("Error")
"""