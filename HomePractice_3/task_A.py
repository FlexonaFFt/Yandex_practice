numOfMemb = int(input())
favoriteMembsSongs = set()
for _ in range(numOfMemb):
    favoriteSongsCnt = int(input())
    membSongsLst = set(input().split())

    if not favoriteMembsSongs:
        favoriteMembsSongs.update(membSongsLst)
    
    favoriteSongsDel = [song for song in favoriteMembsSongs if song not in membSongsLst]

    for song in favoriteSongsDel:
        favoriteMembsSongs.remove(song)
    
print(len(favoriteMembsSongs))
print(' '.join(sorted(favoriteMembsSongs)))

'''
Ввод данных:
Программа начинается с чтения количества людей в
группе numOfMemb. Затем идет цикл по количеству 
участников группы.

Обработка предпочтений:
Для каждого участника сначала считывается количе
ство его любимых треков favoriteSongsCnt. Затем 
считывается список этих треков membSongsLst.

Формирование общего плейлиста:
Используется множество favoriteMembsSongs для хр
анения общих любимых треков всех участников. Есл
и это первый участник, то все его треки добавляю
тся в общий плейлист. Далее происходит фильтраци
я общего плейлиста, удаляются треки, которые не 
входят в плейлист текущего участника.

Вывод результата:
После обработки всех участников выводится количе
ство треков, которые понравились всем участникам.
Затем выводится отсортированный список этих трек
ов через пробел.
'''