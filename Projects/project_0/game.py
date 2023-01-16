"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    max_limit = 101
    min_limit = 1
    number = np.random.randint(1, 101)
    
    while True:
        if count > 20:
            break
        count += 1
        middle = round((max_limit + min_limit)/2)  # предполагаемое число
        if number == middle:
            break  # выход из цикла если угадали
        elif number > middle:
            min_limit = middle
        else:
            max_limit = middle
      
    return(count)


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Среднее количество попыток {score}')
    
    return(score)

print(score_game(random_predict))


if __name__ == "__main__":
    # RUN
    score_game(random_predict)