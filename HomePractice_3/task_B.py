def check_anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return "YES"
    else:
        return "NO"
    
str1 = input().strip()
str2 = input().strip()

print(check_anagram(str1, str2))

'''
Этот код определяет функцию check_anagram, 
которая сравнивает отсортированные символы
двух строк. Если отсортированные строки ра
вны, то строки являются анаграммами, и фун
кция возвращает "YES", иначе "NO". После э
того вводятся две строки, и результат пров
ерки выводится на экран.
'''