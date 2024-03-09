"""
g1, g2 = map(int, input().split(":"))
g3, g4 = map(int, input().split(":"))
counter_1, counter_2 = 0, 0
position = int(input())"""

'''
# Считываем вводные данные
first_match_score = input().split(':')
second_match_score = input().split(':')
location = int(input())

# Переводим строки в числа
goals_first_team = int(first_match_score[0])
goals_second_team = int(first_match_score[1])
current_goals_first_team = int(second_match_score[0])
current_goals_second_team = int(second_match_score[1])

# Проверяем, где играла первая команда в первом матче
if location == 1:
    # Вычисляем разницу в голах для победы без дополнительного времени
    needed_goals = max(0, current_goals_second_team - goals_first_team + 1)
else:
    # Вычисляем разницу в голах для победы без дополнительного времени
    needed_goals = max(0, current_goals_first_team - goals_second_team + 1)

# Выводим необходимое количество мячей
print(needed_goals)'''


'''
def goals_to_win(score1, score2, location):
    g1, g2 = map(int, score1.split(':'))
    g3, g4 = map(int, score2.split(':'))
    
    if location == 1:
        goals_needed = max(0, g4 - g1 + 1)
    else:
        goals_needed = max(0, g3 - g2 + 1)
    
    return goals_needed

# Ввод данных
score1 = input()
score2 = input()
location = int(input())

# Вызов функции и вывод результата
print(goals_to_win(score1, score2, location))'''

def main():
    # OK
    # сложность O(1)
    g1, g2 = map(int, input().split(':'))  # G1 — число мячей, забитых первой командой,
    # а G2 "— число мячей, забитых второй командой
    cur_1, cur_2 = map(int, input().split(':'))  # аналогично для 2-го матча

    l = int(input())  # 1, если первую игру первая команда провела «дома», или 2, если «в гостях»
    is_g1_guest = 0  # 1, если текущая игра в гостях для первой команды, иначе 0
    guest_goals1, guest_goals2 = 0, 0  # кол-во голов в гостях для первой команды

    # рассматриваем два случая
    if l == 1:
        guest_goals2 += g2
        guest_goals1 += cur_1
        is_g1_guest = 1
    elif l == 2:
        guest_goals1 += g1
        guest_goals2 += cur_2

    # теперь g1 и g2 - общее число голов
    g1 += cur_1
    g2 += cur_2

    if g2 - g1 < 0:  # уже победа
        print(0)
        return

    if guest_goals1 + (g2 - g1) * is_g1_guest > guest_goals2:
        # если счёт равный и кол-во голов в гостях больше у 1-ой команды
        print(g2 - g1)
    else:
        print(g2 - g1 + 1)


if __name__ == '__main__':
    main()

'''
def result(x1, x2, y1, y2, flag):
    if x1 + y1 > x2 + y2:
        return True
    elif x1 + y1 < x2 + y2:
        return False
    else:
        if (flag == 2 and x1 > y2) or (flag == 1 and y1 > x2):
            return True
        else:
            return False


x1, x2 = map(int, input().split(':'))
y1, y2 = map(int, input().split(':'))
flag = int(input()) # 2 - первая игра в гостях
c = 0
while(not result(x1, x2, y1, y2, flag)):
    c += 1
    y1 += 1
print(c)'''