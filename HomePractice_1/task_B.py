"""
g1, g2 = map(int, input().split(":"))
g3, g4 = map(int, input().split(":"))
counter_1, counter_2 = 0, 0
position = int(input())"""


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
print(needed_goals)


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