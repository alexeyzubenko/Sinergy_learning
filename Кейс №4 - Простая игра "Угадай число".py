import random

def simple_guessing_game():
    """
    Основная функция для простой игры "Угадай число".
    """
    # 1. Загадываем случайное число и устанавливаем лимит попыток
    secret_number = random.randint(1, 100)
    max_attempts = 5  # Ограничиваем количество попыток
    attempts = 0

    print("--- Простая игра 'Угадай число' ---")
    print(f"Я загадал число от 1 до 100. У тебя есть {max_attempts} попыток.")

    # Основной цикл игры
    while attempts < max_attempts:
        # 2. Запрашиваем ввод у пользователя
        try:
            guess_str = input(f"\nПопытка #{attempts + 1}: Введи свое число: ")
            guess = int(guess_str)
        except ValueError:
            print("Ошибка: пожалуйста, введи целое число.")
            continue # Пропускаем остаток цикла и переходим к следующей попытке

        attempts += 1

        # 3. Проверяем предположение и даем подсказку
        if guess < secret_number:
            print("Слишком маленькое число.")
        elif guess > secret_number:
            print("Слишком большое число.")
        else:
            # 4. Пользователь угадал
            print(f"🎉 Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
            return # Завершаем функцию ( и игру)

    # 5. Если цикл завершился, значит, попытки закончились
    print("\n--- Игра окончена ---")
    print(f"Увы, у тебя закончились попытки. Я загадывал число {secret_number}.")

# Запуск игры
if __name__ == "__main__":
    simple_guessing_game()
