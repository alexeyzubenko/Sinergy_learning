def is_positive_integer(value):
    # Проверяем, является ли строка числом и целым положительным
    try:
        number = int(value)  # Пробуем превратить строку в число
        if number <= 0:  # Проверяем, что число больше нуля
            return False
        return True
    except ValueError:  # Если не получилось превратить в число
        return False


# Основной цикл программы
while True:
    # Запрашиваем ввод у пользователя
    user_input = input("Пожалуйста, введите положительное целое число: ")

    # Проверяем, корректен ли ввод
    if is_positive_integer(user_input):
        number = int(user_input)  # Превращаем строку в число
        print(f"Отлично! Вы ввели число: {number}")
        break  # Выходим из цикла, если всё правильно
    else:
        print("Ошибка! Пожалуйста, введите только положительное целое число (например, 1, 2, 3).")

print("Программа завершена.")
