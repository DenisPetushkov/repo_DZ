print("Вас приветствует программа по переводу времени!")
t = int(input("Введите число в секундах"))
hour = t // 3600
min = (t - hour * 3600) // 60
sec = t - (hour * 3600 + min * 60)
print(f"Полченое время в формате чч:мм:сс -> {hour}:{min}:{sec}")
# как записать время в формате: 00:00:00,  я не понял
