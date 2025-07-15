import random

# --- Настройки игры ---
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 10


def display_instructions():
    """Выводит на экран приветствие и правила игры."""
    print("=============================================")
    print("      Добро пожаловать в игру 'Угадай число'!")
    print("=============================================")
    print(f"Я загадал целое число от {MIN_NUMBER} до {MAX_NUMBER}.")
    print(f"У вас есть {MAX_ATTEMPTS} попыток, чтобы его угадать.")
    print("После каждой попытки я скажу, 'слишком много' или 'слишком мало'.")
    print("Удачи!")
    print("---------------------------------------------")


def get_user_guess(prompt):
    """
    Запрашивает число у пользователя и обрабатывает ошибки ввода.

    Возвращает:
        int: Число, введенное пользователем.
    """
    while True:
        try:
            guess_str = input(prompt)
            guess_int = int(guess_str)
            if MIN_NUMBER <= guess_int <= MAX_NUMBER:
                return guess_int
            else:
                print(f"Ошибка: пожалуйста, введите число в диапазоне от {MIN_NUMBER} до {MAX_NUMBER}. 範圍")
        except ValueError:
            print("Ошибка: введено нечисловое значение. Пожалуйста, введите целое число. ")


def give_hint(attempts_left, secret_number):
    """
    Предоставляет подсказку, если у игрока осталось мало попыток.
    """
    if attempts_left == 3:  # Даем подсказку, когда осталось 3 попытки
        if secret_number % 2 == 0:
            print("Подсказка: загаданное число - чётное.")
        else:
            print("Подсказка: загаданное число - нечётное.")


def play_game():
    """Основная функция, запускающая один раунд игры."""
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts_made = 0

    display_instructions()

    while attempts_made < MAX_ATTEMPTS:
        attempts_left = MAX_ATTEMPTS - attempts_made
        print(f"\nПопытка №{attempts_made + 1}. Осталось попыток: {attempts_left}")

        # Даем подсказку в определенный момент
        give_hint(attempts_left, secret_number)

        user_guess = get_user_guess("Ваше предположение: ")

        attempts_made += 1

        if user_guess < secret_number:
            print("Слишком мало! Попробуйте число побольше.")
        elif user_guess > secret_number:
            print("Слишком много! Попробуйте число поменьше.")
        else:
            print("\n=============================================")
            print(f"Поздравляю! Вы угадали! Загаданное число было {secret_number}.")
            print(f"Вам потребовалось {attempts_made} попыток.")
            print("=============================================")
            return  # Выход из функции, так как игра выиграна

    # Этот код выполнится, только если цикл завершился (попытки закончились)
    print("\n=============================================")
    print(f"Увы, у вас закончились попытки. Вы проиграли.")
    print(f"Я загадывал число {secret_number}.")
    print("=============================================")


def main():
    """Главное меню игры, управляющее повторными играми."""
    while True:
        play_game()

        play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
        if play_again not in ["да", "yes", "д", "y"]:
            print("Спасибо за игру! До скорой встречи!")
            break


# --- Запуск игры ---
if __name__ == "__main__":
    main()
