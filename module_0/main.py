import numpy as np


def score_game(game_core_v1):
    '''
    Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    '''
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)

    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core_v1(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return(score)


def game_core_v4(number):
    '''
    Функция играет в угадайку.
    Пытается угадать переданное число от 0 до 100.
    Алгоритм поиска - каждый раз сужаем область поиска - основываясь на том,
    что загаданное число больше или меньше предсказанного.
    Возвращает количество попыток, за которое удалось угадать.
    Параметры:
        number - загаданное число
    '''
    count = 1
    lo, hi = 1, 100  # нижняя и верхняя граница области поиска
    predict = 50

    while number != predict:
        count += 1

        # уменьшаем область поиска
        if number > predict:
            lo = predict+1
        elif number < predict:
            hi = predict-1

        predict = lo + (hi-lo)//2  # берем середину от новой области поиска

    return count  # выход из цикла, если угадали


if __name__ == '__main__':
    # Проверяем
    score_game(game_core_v4)
