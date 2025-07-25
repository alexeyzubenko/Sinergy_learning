import math

def calculate_factorial():
    """
    Запрашивает у пользователя ввод, вычисляет факториал
    и обрабатывает возможные ошибки.
    """
    try:
        # Запрашиваем у пользователя ввод числа
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)

        # Проверяем, является ли число отрицательным
        if number < 0:
            print("Ошибка: Факториал не определен для отрицательных чисел.")
        else:
            # Вычисляем факториал с помощью оптимизированной функции из библиотеки math
            result = math.factorial(number)
            print(f"Факториал числа {number} равен {result}.")

    except ValueError:
        # Обрабатываем ошибку, если введено нечисловое значение
        print("Ошибка: Введено не целое число. Пожалуйста, попробуйте снова.")
    except Exception as e:
        # Обрабатываем другие возможные ошибки
        print(f"Произошла непредвиденная ошибка: {e}")

# Запускаем основную функцию
if __name__ == "__main__":
    calculate_factorial()
