import random

# Функция для угадывания числа
def guess_number():
    # Загадываем случайное число
    secret_number = random.randint(1, 100)
    
    # Инициализируем начальные значения диапазона
    low = 1
    high = 100
    attempts = 0

    while True:
        # Предполагаем, что число находится посередине диапазона
        guess = (low + high) // 2
        attempts += 1
        
        # Проверяем, угадали ли мы число
        if guess == secret_number:
            print(f"Компьютер угадал число {secret_number} за {attempts} попыток.")
            break
        elif guess < secret_number:
            print(f"Компьютер думает, что загаданное число больше {guess}.")
            low = guess + 1
        else:
            print(f"Компьютер думает, что загаданное число меньше {guess}.")
            high = guess - 1

# Запускаем игру
guess_number()
