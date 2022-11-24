# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит некоторое кол-во конфет, например 220.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, которые точно определят победу.

from colorama import Fore, Back, Style

# Выбор мода игры
def game_mode(g_mode: int) -> str:
    if g_mode == 1:
        player_1 = input("Первый игрок, введите Ваше имя: ")
        player_2 = input("Второй игрок, введите Ваше имя: ")
        return player_1, player_2
    elif g_mode == 2:
        print("Хорошо, я поиграю с тобой!")
        player_1 = input("Введите Ваше имя: ")
        player_2 = "бот"
        return player_1, player_2
    else:
        print("Не верно задан параметр игры")


# Симуляция броска кубика
import random

def rand_move(player_1: str, player_2: str) -> str:
    first = player_1
    second = player_2
    rand_res_1 = random.randint(1, 20)
    rand_res_2 = random.randint(1, 20)
    if rand_res_1 != rand_res_2:
        if rand_res_1 > rand_res_2:
            print(f"{player_1} ходит первым")
            first = player_1
            second = player_2  
        else:
            print(f"{player_2}, ходит первым")
            first = player_2
            second = player_1
    else:
        rand_res_1 += 1
        first = player_1
        second = player_2
    print(f"{player_1} бросил 1D20 и выбросил {rand_res_1}, {player_2} бросил 1D20 и выбросил {rand_res_2}")
    return first, second

candies = 220
max_move = 28
left_win = candies % (max_move + 1)
current_step = 0

print(f"Правила игры: на столе находится {candies} конфет. За один ход можно взять от 1 до {max_move} конфет.")
print("Выиграет тот, кто возьмет последние конфеты со стола.")

# Симулятор хода (для победы, на предпоследнем ходу должно остаться max_move + 1 конфета)
def game_step(player: str, current_step: int) -> int:
    if player == "бот":
        if current_step == 0:
            step = candies % (max_move + 1)
        else:
            step = (max_move + 1) - current_step
        print(f"Я беру {step} конфет")
        return step
    else:
        step = int(input(f"{player}, сколько конфет ты возьмешь?  "))
        if 0 < step < max_move + 1:
            return step
        else:
            print(f"Такое число нарушает условия игры.")

game = int(input("Для игры с другим игроком, введите 1, для игры с компьютером введите 2:  "))
player_1, player_2 = game_mode(game)
print (f"Играет {player_1} против {player_2}!")
first, second = rand_move(player_1, player_2)

while candies > max_move:
    current_step = game_step(first, current_step)
    candies -= current_step
    print(Fore.BLUE + f"На столе осталось {candies} конфет.")
    print(Style.RESET_ALL)
    if candies <= max_move:
        print(Back.GREEN + f"{first}, какой ты молодец! Победа за тобой! Ведь на столе всего лишь {candies} конфет.") 
        print(Style.RESET_ALL)
        break
    current_step = game_step(second, current_step)
    candies -= current_step
    print(f"На столе осталось {candies} конфет.")
    if candies <= max_move:
        print(Back.GREEN + f"{first}, какой ты молодец! Победа за тобой! Ведь на столе всего лишь {candies} конфет.") 
        print(Style.RESET_ALL)
