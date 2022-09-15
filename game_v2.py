"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    count = 0
    max1 = 101
    min1 = 1
    number = np.random.randint(1, 101)
    while True:
        if count > 20:
            break
        count += 1
        mid1 = round((max1 + min1)/2)  # предполагаемое число
        if number == mid1:
            break  # выход из цикла если угадали
        elif number > mid1:
            min1 = mid1
        else:
            max1 = mid1
    return(count)


def score_game(random_predict) -> int:
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    return(score)




if __name__ == "__main__":
    # RUN
    score_game(random_predict)
