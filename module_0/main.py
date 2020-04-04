import numpy as np

def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v4(number):
    
    count = 0
    lo,hi = 1,101
    predict = np.random.randint(lo,hi)
    while number != predict:
        count+=1
        if number > predict: 
            lo = predict
        elif number < predict: 
            hi = predict
        predict = lo + (hi-lo)//2
        
    return count # выход из цикла, если угадали

if __name__ == '__main__':
    # Проверяем
    score_game(game_core_v4)
    